from uuid import UUID
from src.propiedadesalpes.config.db import db
from src.propiedadesalpes.modulos.propiedad.dominio.repositorios import RepositorioPropiedades
from src.propiedadesalpes.modulos.propiedad.dominio.entidades import Propiedad
from src.propiedadesalpes.modulos.propiedad.dominio.fabricas import FabricaHistorico
from src.propiedadesalpes.seedwork.dominio.entidades import Entidad
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad

class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_historicos: FabricaHistorico = FabricaHistorico()

    @property
    def fabrica_historicos(self):
        return self._fabrica_historicos
    
    def obtener_por_campo(self, estado: str) -> list[Propiedad]:
        list_propiedad_dto = db.session.query(PropiedadDTO).filter_by(estado_propiedad=estado)
        list_transaction: list[Propiedad] = list(map(lambda propiedad_dto: self.fabrica_historicos.crear_objeto(propiedad_dto, MapeadorPropiedad()), list_propiedad_dto))
        return list_transaction

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_historicos.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)
        db.session.commit()

    def actualizar(self, propiedad: Propiedad):
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id_propiedad=propiedad.id_propiedad).first()
        propiedad_dto.nombre_cliente = propiedad.nombre_propiedad
        propiedad_dto.estado_propiedad = propiedad.estado_propiedad
        propiedad_dto.cliente_propiedad = propiedad.cliente_propiedad
        db.session.add(propiedad_dto)
        db.session.commit()

    def eliminar(self, id_propiedad: str):
        # TODO
        raise NotImplementedError
    
    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id_propiedad=str(id)).first()
        return self.fabrica_historicos.crear_objeto(propiedad_dto, MapeadorPropiedad())
    
    def obtener_todos(self) -> list[Propiedad]:
        raise NotImplementedError