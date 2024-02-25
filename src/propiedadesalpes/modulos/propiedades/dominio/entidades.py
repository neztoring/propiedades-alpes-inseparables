from __future__ import annotations
from dataclasses import dataclass, field

from src.propiedadesalpes.seedwork.dominio.entidades import AgregacionRaiz
from src.propiedadesalpes.modulos.propiedades.dominio.eventos import TransaccionCreada

import uuid

@dataclass
class Transaccion(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)

    def crear_transaccion(self, transaccion: Transaccion):
        self.id_propiedad = transaccion.id_propiedad

        self.agregar_evento(TransaccionCreada(id_propiedad=self.id))

