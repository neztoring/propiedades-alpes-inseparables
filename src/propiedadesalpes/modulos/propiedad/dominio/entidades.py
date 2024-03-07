from __future__ import annotations
from dataclasses import dataclass, field

from src.propiedadesalpes.seedwork.dominio.entidades import AgregacionRaiz
from src.propiedadesalpes.modulos.propiedad.dominio.eventos import PropiedadCreada

import uuid

@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    nombre_propiedad: str = field(hash=True, default=None)
    estado_propiedad: str = field(hash=True, default=None)
    cliente_propiedad: str = field(hash=True, default=None)

    def crear_propiedad(self, propiedad: Propiedad):
        self.id_propiedad = propiedad.id_propiedad
        self.nombre_propiedad = propiedad.nombre_propiedad
        self.estado_propiedad = propiedad.estado_propiedad
        self.cliente_propiedad = propiedad.cliente_propiedad

        self.agregar_evento(PropiedadCreada(
            id_propiedad=self.id_propiedad,
            nombre_propiedad=self.nombre_propiedad,
            estado_propiedad=self.estado_propiedad,
            cliente_propiedad=self.cliente_propiedad
        ))

