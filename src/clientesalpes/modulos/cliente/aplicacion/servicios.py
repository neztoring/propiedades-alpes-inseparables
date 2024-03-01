from typing import Dict, Any

from src.clientesalpes.seedwork.aplicacion.servicios import Servicio
from src.clientesalpes.modulos.cliente.infraestructura.fabricas import FabricaRepositorio
from src.clientesalpes.modulos.cliente.dominio.repositorios import RepositorioClientes
from src.clientesalpes.modulos.cliente.dominio.fabricas import FabricaHistorico
from .dto import ClienteDTO

from .mapeadores import MapeadorCliente
from ..dominio.entidades import Cliente


class ServicioCliente(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_historicos: FabricaHistorico = FabricaHistorico()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_historicos(self):
        return self._fabrica_historicos

    def crear_cliente(self, cliente_dto: ClienteDTO) -> ClienteDTO:
        mapeador_cliente = MapeadorCliente()
        cliente: Cliente = self.fabrica_historicos.crear_objeto(cliente_dto, mapeador_cliente)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        repositorio.agregar(cliente)

        return self.fabrica_historicos.crear_objeto(cliente, mapeador_cliente)

    def obtener_cliente_por_id(self, id) -> ClienteDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        return repositorio.obtener_por_id(id).__dict__

    def obtener_todos(self) -> list[ClienteDTO]:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        return repositorio.obtener_todos()