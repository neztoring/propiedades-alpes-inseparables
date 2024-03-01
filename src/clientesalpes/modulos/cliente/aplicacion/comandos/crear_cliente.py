from src.clientesalpes.seedwork.aplicacion.comandos import Comando
from src.clientesalpes.modulos.cliente.aplicacion.dto import ClienteDTO
from .base import CrearClienteBaseHandler
from dataclasses import dataclass
from src.clientesalpes.seedwork.aplicacion.comandos import ejecutar_comando as comando
from src.clientesalpes.modulos.cliente.dominio.entidades import Cliente
from src.clientesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.clientesalpes.modulos.cliente.aplicacion.mapeadores import MapeadorCliente
from src.clientesalpes.modulos.cliente.infraestructura.repositorios import RepositorioClientes

@dataclass
class CrearCliente(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    id_cliente: str
    nombre_cliente: str
    tipo_cliente: str

class CrearClienteHandler(CrearClienteBaseHandler):
    def handle(self, comando: CrearCliente):
        cliente_dto = ClienteDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            id_cliente=comando.id_cliente,
            nombre_cliente=comando.nombre_cliente,
            tipo_cliente=comando.tipo_cliente
        )

        cliente: Cliente = self._fabrica_clientes.crear_objeto(cliente_dto, MapeadorCliente())
        cliente.crear_cliente(cliente)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, cliente)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register
def ejecutar_comando_crear_cliente(comando: CrearCliente):
    handler = CrearClienteHandler()
    handler.handle(comando=comando)