# app/__init__.py
from flask import Flask
from app.routes import main
from app.utils import validate_environment

def create_app():
    """
    Factory function para crear la aplicación Flask
    """
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    # Configuración básica
    app.config['SECRET_KEY'] = 'dev-key-change-in-production'
    app.config['JSON_AS_ASCII'] = False  # Para caracteres españoles
    
    # Registrar el blueprint con las rutas
    app.register_blueprint(main)
    
    # Validar variables de entorno al iniciar
    with app.app_context():
        validate_environment()
    
    return app
