# pokeneas_app/__init__.py
import os
from flask import Flask
from pokeneas_app.routes import main
from pokeneas_app.utils import validate_environment

def create_app():
    """
    Factory function para crear la aplicación Flask
    """
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    # Configuración básica usando variables de entorno
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    app.config['JSON_AS_ASCII'] = False  # Para caracteres españoles
    
    # Registrar el blueprint con las rutas
    app.register_blueprint(main)
    
    # Validar variables de entorno al iniciar
    with app.app_context():
        validate_environment()
    
    return app
