import os
from flask import Flask
import threading

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    pass

def comenzar_consumidor():
    import threading
    import src.propiedadesalpes.modulos.propiedad.infraestructura.consumidores as propiedad

    # Suscripción a eventos
    threading.Thread(target=propiedad.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=propiedad.suscribirse_a_comandos).start()

# Init la aplicacion de Flask
app = Flask(__name__, instance_relative_config=True)

# Configuracion de BD
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'propiedades_database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ef66b23d-bf07-4eb5-a8ea-1d6262bbc703'
app.config['SESSION_TYPE'] = 'filesystem'

    # Inicializa la DB
from src.propiedadesalpes.config.db import init_db
init_db(app)

from src.propiedadesalpes.config.db import db

importar_modelos_alchemy()

from . import propiedades
from ...propiedadesalpes.api import propiedades

app.register_blueprint(propiedades.bp)

with app.app_context():
    db.create_all()
    if not app.config.get('TESTING'):
        comenzar_consumidor()

@app.route("/health-status")
def health():
    return {"status": "up"}
