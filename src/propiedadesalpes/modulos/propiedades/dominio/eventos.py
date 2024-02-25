from __future__ import annotations
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class TransaccionCreada(EventoDominio):
    id_transaccion: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
