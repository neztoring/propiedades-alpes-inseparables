from src.clientesalpes.config.db import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Table, String

import uuid

Base = db.declarative_base()

class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    id_cliente = db.Column(db.String, primary_key=True, nullable=False)
    nombre_cliente = db.Column(db.String, primary_key=False, nullable=False)
    tipo_cliente = db.Column(db.String, primary_key=False, nullable=False)