from __future__ import annotations
from dataclasses import dataclass, field

from src.clientesalpes.seedwork.dominio.entidades import AgregacionRaiz
from src.clientesalpes.modulos.cliente.dominio.eventos import ClienteCreada
from src.clientesalpes.modulos.cliente.dominio.comandos import CrearPropiedad

import uuid

@dataclass
class Cliente(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    nombre_cliente: str = field(hash=True, default=None)
    tipo_cliente: str = field(hash=True, default=None)

    def crear_cliente(self, cliente: Cliente):
        self.id_cliente = cliente.id_cliente
        self.nombre_cliente = cliente.nombre_cliente
        self.tipo_cliente = cliente.tipo_cliente

        self.agregar_evento(ClienteCreada(id_cliente=self.id,nombre_cliente=self.nombre_cliente, tipo_cliente=self.tipo_cliente))

@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    nombre_propiedad :str = field(hash=True, default=None)
    estado_propiedad:str = field(hash=True, default=None)
    cliente_propiedad: str = field(hash=True, default=None)

    def crear_propiedad(self, propiedad: Propiedad):
        self.id_propiedad = propiedad.id_propiedad
        self.nombre_propiedad = propiedad.nombre_propiedad
        self.estado_propiedad = propiedad.estado_propiedad
        self.cliente_propiedad = propiedad.cliente_propiedad

        self.agregar_comando(CrearPropiedad(id_propiedad=self.id_propiedad, nombre_propiedad=self.nombre_propiedad, estado_propiedad=self.estado_propiedad, id_cliente=self.cliente_propiedad))