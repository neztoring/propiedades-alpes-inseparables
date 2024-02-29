from src.propiedadesalpes.seedwork.aplicacion.comandos import ComandoHandler
from src.propiedadesalpes.modulos.propiedad.infraestructura.fabricas import FabricaRepositorio
from src.propiedadesalpes.modulos.propiedad.dominio.fabricas import _FabricaPropiedad

class CrearPropiedadBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: _FabricaPropiedad = _FabricaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades