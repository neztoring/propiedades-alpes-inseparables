from src.clientesalpes.seedwork.aplicacion.comandos import ComandoHandler
from src.clientesalpes.modulos.cliente.infraestructura.fabricas import FabricaRepositorio
from src.clientesalpes.modulos.cliente.dominio.fabricas import _FabricaCliente

class CrearClienteBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_clientes: _FabricaCliente = _FabricaCliente()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes
    
class CrearPropiedadBaseHandler(ComandoHandler):
    ...