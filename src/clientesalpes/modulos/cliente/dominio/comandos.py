from __future__ import annotations
from dataclasses import dataclass, field
from src.clientesalpes.seedwork.dominio.comandos import (ComandoDominio)

@dataclass
class CrearPropiedad(ComandoDominio):
    id_propiedad: str = None
    id_cliente: str = None
    nombre_propiedad: str = None
    estado_propiedad: str = None
