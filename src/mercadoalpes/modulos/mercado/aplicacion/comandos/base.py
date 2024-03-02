from src.mercadoalpes.seedwork.aplicacion.comandos import ComandoHandler
from src.mercadoalpes.modulos.mercado.infraestructura.fabricas import FabricaRepositorio
from src.mercadoalpes.modulos.mercado.dominio.fabricas import FabricaTransaccion

class CrearTransaccionBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_transacciones: FabricaTransaccion = FabricaTransaccion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_transacciones(self):
        return self._fabrica_transacciones