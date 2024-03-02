from src.clientesalpes.modulos.cliente.dominio.entidades import Cliente
from src.clientesalpes.seedwork.dominio.repositorios import Mapeador
from .dto import Cliente as ClienteDTO

class MapeadorCliente(Mapeador):

    def obtener_tipo(self) -> type:
        return Cliente.__class__
    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        
        cliente_dto = ClienteDTO()
        cliente_dto.fecha_creacion = entidad.fecha_creacion
        cliente_dto.fecha_actualizacion = entidad.fecha_actualizacion
        cliente_dto.id = str(entidad.id)
        cliente_dto.id_cliente = str(entidad.id_cliente)
        cliente_dto.nombre_cliente = str(entidad.nombre_cliente)
        cliente_dto.tipo_cliente = str(entidad.tipo_cliente)

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente = Cliente(dto.id, dto.fecha_creacion, dto.fecha_actualizacion, dto.id_cliente, dto.nombre_cliente, dto.tipo_cliente)
        cliente.id_cliente = dto.id_cliente
        cliente.nombre_cliente = dto.nombre_cliente
        cliente.tipo_cliente = dto.tipo_cliente
        return cliente