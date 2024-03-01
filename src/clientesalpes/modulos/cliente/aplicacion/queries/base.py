from src.clientesalpes.seedwork.aplicacion.queries import QueryHandler
from src.clientesalpes.modulos.cliente.infraestructura.fabricas import FabricaRepositorio
from src.clientesalpes.modulos.cliente.dominio.fabricas import _FabricaCliente

class ClienteQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self.fabrica_clientes: _FabricaCliente = _FabricaCliente()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_transacciones(self):
        return self.fabrica_clientes    