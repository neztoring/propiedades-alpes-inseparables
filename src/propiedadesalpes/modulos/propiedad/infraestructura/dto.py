from src.propiedadesalpes.config.db import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Table, String

import uuid

Base = db.declarative_base()

class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    id_propiedad = db.Column(db.String, primary_key=True, nullable=False)
    nombre_propiedad = db.Column(db.String, primary_key=False, nullable=False)
    estado_propiedad = db.Column(db.String, primary_key=False, nullable=False)
    cliente_propiedad = db.Column(db.String, primary_key=False, nullable=False)