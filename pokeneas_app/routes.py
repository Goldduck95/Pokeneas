# pokeneas_app/routes.py
from flask import Blueprint, jsonify, render_template
from pokeneas_app.models import get_random_pokenea, get_all_pokeneas
from pokeneas_app.utils import get_container_id, get_s3_image_url

# Crea un Blueprint para organizar las rutas
main = Blueprint('main', __name__)


@main.route('/')
def index():
    """
    Página principal con información del proyecto
    """
    return render_template('index.html')


@main.route('/api/pokenea')
def api_pokenea():
    """
    Ruta JSON: devuelve un Pokenea aleatorio con información básica
    y el ID del contenedor que procesa la petición.
    """
    pokenea = get_random_pokenea()
    
    response = pokenea.to_json_response()
    response['container_id'] = get_container_id()
    
    return jsonify(response)


@main.route('/pokenea')
def mostrar_pokenea():
    """
    Ruta HTML: muestra la imagen y frase filosófica de un Pokenea aleatorio
    junto con el ID del contenedor.
    """
    pokenea = get_random_pokenea()
    imagen_url = get_s3_image_url(pokenea.imagen)
    container_id = get_container_id()
    
    return render_template(
        'pokenea.html',
        pokenea=pokenea,
        imagen_url=imagen_url,
        container_id=container_id
    )


@main.route('/api/pokeneas')
def api_all_pokeneas():
    """
    Ruta extra: devuelve todos los Pokeneas disponibles
    (útil para debugging o consultar la colección completa)
    """
    pokeneas = get_all_pokeneas()
    return jsonify({
        'total': len(pokeneas),
        'pokeneas': [p.to_dict() for p in pokeneas],
        'container_id': get_container_id()
    })


@main.route('/health')
def health_check():
    """
    Ruta de health check para Docker Swarm
    """
    return jsonify({
        'status': 'healthy',
        'container_id': get_container_id()
    }), 200
