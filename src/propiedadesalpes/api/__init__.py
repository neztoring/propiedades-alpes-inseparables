import os
from flask import Flask

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    pass

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # Inicializa la DB
    from src.propiedadesalpes.config.db import init_db
    init_db(app)

    from src.propiedadesalpes.config.db import db

    importar_modelos_alchemy()

    from . import propiedades

    app.register_blueprint(propiedades.bp)

    with app.app_context():
        db.create_all()
    
    @app.route("/health")
    def health():
        return {"status": "up"}

    return app