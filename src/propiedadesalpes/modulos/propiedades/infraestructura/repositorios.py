from src.propiedadesalpes.config.db import db
from src.propiedadesalpes.modulos.propiedades.dominio.repositorios import RepositorioTransacciones
from src.propiedadesalpes.modulos.propiedades.dominio.entidades import Transaccion
from src.propiedadesalpes.modulos.propiedades.dominio.fabricas import FabricaHistorico
from .dto import Transaccion as TransaccionDTO
from .mapeadores import MapeadorTransaccion
from uuid import UUID

class RepositorioTransaccionesSQLite(RepositorioTransacciones):

    def __init__(self):
        self._fabrica_historicos: FabricaHistorico = FabricaHistorico()

    @property
    def fabrica_historicos(self):
        return self._fabrica_historicos

    def obtener_por_id(self, id: UUID) -> Transaccion:
        transaccion_dto = db.session.query(TransaccionDTO).filter_by(id=str(id)).one()
        return self.fabrica_historicos.crear_objeto(transaccion_dto, MapeadorTransaccion())

    def obtener_todos(self) -> list[Transaccion]:
        # TODO
        raise NotImplementedError

    def agregar(self, transaccion: Transaccion):
        transaccion_dto = self.fabrica_historicos.crear_objeto(transaccion, MapeadorTransaccion())
        db.session.add(transaccion_dto)
        db.session.commit()

    def actualizar(self, transaccion: Transaccion):
        # TODO
        raise NotImplementedError

    def eliminar(self, transaccion_id: UUID):
        # TODO
        raise NotImplementedError