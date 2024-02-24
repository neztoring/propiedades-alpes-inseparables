from src.propiedadesalpes.config.db import db

Base = db.declarative_base()

class Transaccion(db.Model):
    __tablename__ = "transacciones"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    id_propiedad = db.Column(db.String, nullable=False)