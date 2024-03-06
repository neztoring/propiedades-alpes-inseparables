from typing import Dict, Any

from src.propiedadesalpes.seedwork.aplicacion.servicios import Servicio
from src.propiedadesalpes.modulos.propiedad.infraestructura.fabricas import FabricaRepositorio
from src.propiedadesalpes.modulos.propiedad.dominio.repositorios import RepositorioPropiedades
from src.propiedadesalpes.modulos.propiedad.dominio.fabricas import FabricaHistorico
from .dto import PropiedadDTO

from .mapeadores import MapeadorPropiedad
from ..dominio.entidades import Propiedad


class ServicioPropiedad(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_historicos: FabricaHistorico = FabricaHistorico()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_historicos(self):
        return self._fabrica_historicos

    def crear_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:
        mapeador_propiedad = MapeadorPropiedad()
        propiedad: Propiedad = self.fabrica_historicos.crear_objeto(propiedad_dto, mapeador_propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        repositorio.agregar(propiedad)

        return self.fabrica_historicos.crear_objeto(propiedad, mapeador_propiedad)
    
    def actualizar_estado_propiedad(self, propiedad_dto: PropiedadDTO, estado: str) -> PropiedadDTO:
        mapeador_propiedad = MapeadorPropiedad()
        propiedad: Propiedad = self.fabrica_historicos.crear_objeto(propiedad_dto, mapeador_propiedad)
        
        propiedad.estado_propiedad = estado

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        repositorio.actualizar(propiedad)
        
        return self.fabrica_historicos.crear_objeto(propiedad, mapeador_propiedad)


    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        mapeador_propiedad = MapeadorPropiedad()
        return mapeador_propiedad.entidad_a_dto(repositorio.obtener_por_id(id))

    def obtener_todos(self) -> list[PropiedadDTO]:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        return repositorio.obtener_todos()