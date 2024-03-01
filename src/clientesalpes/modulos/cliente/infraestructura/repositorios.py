from src.clientesalpes.config.db import db
from src.clientesalpes.modulos.cliente.dominio.repositorios import RepositorioClientes
from src.clientesalpes.modulos.cliente.dominio.entidades import Cliente
from src.clientesalpes.modulos.cliente.dominio.fabricas import FabricaHistorico
from .dto import Cliente as ClienteDTO
from .mapeadores import MapeadorCliente
from uuid import UUID

class RepositorioClientesSQLite(RepositorioClientes):

    def __init__(self):
        self._fabrica_historicos: FabricaHistorico = FabricaHistorico()

    @property
    def fabrica_historicos(self):
        return self._fabrica_historicos

    def obtener_por_id(self, id: UUID) -> Cliente:
        cliente_dto = db.session.query(ClienteDTO).filter_by(id=str(id)).one()
        return self.fabrica_historicos.crear_objeto(cliente_dto, MapeadorCliente())

    def obtener_todos(self) -> list[Cliente]:
        list_cliente_dto = db.session.query(ClienteDTO)
        list_transaction: list[Cliente] = list(map(lambda cliente_dto: self.fabrica_historicos.crear_objeto(cliente_dto, MapeadorCliente()), list_cliente_dto))
        return list_transaction

    def agregar(self, cliente: Cliente):
        cliente_dto = self.fabrica_historicos.crear_objeto(cliente, MapeadorCliente())
        db.session.add(cliente_dto)
        db.session.commit()

    def actualizar(self, cliente: Cliente):
        # TODO
        raise NotImplementedError

    def eliminar(self, cliente_id: UUID):
        # TODO
        raise NotImplementedError