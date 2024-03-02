from src.propiedadesalpes.seedwork.aplicacion.queries import QueryHandler
from src.propiedadesalpes.modulos.propiedad.infraestructura.fabricas import FabricaRepositorio
from src.propiedadesalpes.modulos.propiedad.dominio.fabricas import FabricaPropiedad

class PropiedadQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades    