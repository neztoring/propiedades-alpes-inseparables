from dataclasses import dataclass, field

from src.propiedadesalpes.seedwork.dominio.entidades import Entidad

@dataclass
class Transaccion(Entidad):
    id_propiedad: str = field(default_factory=str)