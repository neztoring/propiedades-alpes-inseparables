from dataclasses import dataclass, field
from src.mercadoalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class TransaccionDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    id_propiedad: str = field(default_factory=str)
    tipo_transaccion: str = field(default_factory=str)
