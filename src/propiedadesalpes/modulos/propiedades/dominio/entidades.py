from dataclasses import dataclass, field

from src.propiedadesalpes.seedwork.dominio.entidades import Entidad, AgregacionRaiz

@dataclass
class Transaccion(Entidad):
    id_propiedad: str = field(default_factory=str)