from dataclasses import dataclass
from src.clientesalpes.seedwork.aplicacion.queries import Query, QueryResultado
from src.clientesalpes.seedwork.aplicacion.queries import ejecutar_query as query
from src.clientesalpes.modulos.cliente.infraestructura.repositorios import RepositorioClientes
from src.clientesalpes.modulos.cliente.aplicacion.mapeadores import MapeadorCliente
from .base import ClienteQueryBaseHandler

@dataclass
class ObtenerCliente(Query):
    id: str

class ObtenerClienteHandler(ClienteQueryBaseHandler):
    def handle(self, query: ObtenerCliente) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        cliente = self.fabrica_clientes.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorCliente())
        return QueryResultado(resultado=cliente)

@query.register
def ejecutar_query_obtener_cliente(query: ObtenerCliente):
    handler = ObtenerClienteHandler()
    return handler.handle(query=query)



