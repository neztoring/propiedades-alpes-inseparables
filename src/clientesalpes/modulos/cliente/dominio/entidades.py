from __future__ import annotations
from dataclasses import dataclass, field

from src.clientesalpes.seedwork.dominio.entidades import AgregacionRaiz
from src.clientesalpes.modulos.cliente.dominio.eventos import ClienteCreada

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

