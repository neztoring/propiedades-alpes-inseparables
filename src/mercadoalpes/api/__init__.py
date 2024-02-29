import os
from flask import Flask
import threading

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    pass

def comenzar_consumidor():
    import src.mercadoalpes.modulos.mercado.infraestructura.consumidores as propiedades_consumidor
    threading.Thread(target=propiedades_consumidor.suscribirse_a_eventos("eventos-transaccion")).start()

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'ef66b23d-bf07-4eb5-a8ea-1d6262bbc703'
    app.config['SESSION_TYPE'] = 'filesystem'

     # Inicializa la DB
    from src.mercadoalpes.config.db import init_db
    init_db(app)

    from src.mercadoalpes.config.db import db

    importar_modelos_alchemy()

    from . import mercado
    from ...propiedadesalpes.api import propiedades

    app.register_blueprint(mercado.bp)
    app.register_blueprint(propiedades.bp)

    with app.app_context():
        db.create_all()
        consumidor_thread = threading.Thread(target=comenzar_consumidor)
        consumidor_thread.start()
    
    @app.route("/health-status")
    def health():
        return {"status": "up"}

    return app