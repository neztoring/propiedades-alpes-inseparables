from __future__ import annotations
from dataclasses import dataclass, field
from src.propiedadesalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class TransaccionCreada(EventoDominio):
    id_propiedad: str = None
    fecha_creacion: datetime = None
