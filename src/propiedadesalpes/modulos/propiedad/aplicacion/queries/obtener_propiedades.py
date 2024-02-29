from dataclasses import dataclass
from src.propiedadesalpes.seedwork.aplicacion.queries import Query, QueryResultado
from src.propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query as query
from src.propiedadesalpes.modulos.propiedad.infraestructura.repositorios import RepositorioPropiedades
from src.propiedadesalpes.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedad
from .base import PropiedadQueryBaseHandler

@dataclass
class ObtenerPropiedades(Query):
    estado: str

class ObtenerPropiedadesHandler(PropiedadQueryBaseHandler):
    def handle(self, query: ObtenerPropiedades) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        propiedades = [] 
        result = repositorio.obtener_por_campo(query.estado)
        if result:
            for record in result:
                propiedades.append(self.fabrica_propiedades.crear_objeto(record, MapeadorPropiedad()))
        return QueryResultado(resultado=propiedades)

@query.register
def ejecutar_query_obtener_propiedades(query: ObtenerPropiedades):
    handler = ObtenerPropiedadesHandler()
    return handler.handle(query=query)


