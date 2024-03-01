from dataclasses import dataclass, field
from src.clientesalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ClienteDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    id_cliente: str = field(default_factory=str)
    nombre_cliente: str = field(default_factory=str)
    tipo_cliente: str = field(default_factory=str)