from dataclasses import dataclass

from src.propiedadesalpes.seedwork.dominio.entidades import Entidad

@dataclass
class Transaccion(Entidad):
    def __init__(self):
        self.id_propiedad = None