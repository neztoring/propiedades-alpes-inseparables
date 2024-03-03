from __future__ import annotations
from dataclasses import dataclass, field
from src.clientesalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class ClienteCreada(EventoDominio):
    id_cliente: str = None
    nombre_cliente: str = None
    tipo_cliente: str = None
    fecha_creacion: datetime = None
