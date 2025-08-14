from flask import Flask
from .config import Config

def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Carga la configuración desde el objeto Config
    app.config.from_object(Config)
    
    # Importa y registra el Blueprint
    from .api.routes import api_bp
    app.register_blueprint(api_bp) 
    
    return app