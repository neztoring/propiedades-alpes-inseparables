from dataclasses import dataclass
from src.mercadoalpes.seedwork.aplicacion.queries import Query, QueryResultado
from src.mercadoalpes.seedwork.aplicacion.queries import ejecutar_query as query
from src.mercadoalpes.modulos.mercado.infraestructura.repositorios import RepositorioTransacciones
from src.mercadoalpes.modulos.mercado.aplicacion.mapeadores import MapeadorTransaccion
from .base import TransaccionQueryBaseHandler

@dataclass
class ObtenerTransaccion(Query):
    id: str

class ObtenerTransaccionHandler(TransaccionQueryBaseHandler):
    def handle(self, query: ObtenerTransaccion) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)
        transaccion = self.fabrica_transacciones.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorTransaccion())
        return QueryResultado(resultado=transaccion)

@query.register
def ejecutar_query_obtener_transaccion(query: ObtenerTransaccion):
    handler = ObtenerTransaccionHandler()
    return handler.handle(query=query)



