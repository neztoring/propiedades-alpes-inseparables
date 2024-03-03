from .dto import ClienteDTO, PropiedadDTO
from src.clientesalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from src.clientesalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from src.clientesalpes.modulos.cliente.dominio.entidades import Cliente

from datetime import datetime


class MapeadorClienteDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> ClienteDTO:
        cliente_dto = ClienteDTO(id_cliente=externo.get("id_cliente"),
            nombre_cliente=externo.get("nombre_cliente"),
            tipo_cliente=externo.get("tipo_cliente"))
        return cliente_dto

    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        return dto.__dict__


class MapeadorCliente(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        id_cliente = str(entidad.id_cliente)
        nombre_cliente = str(entidad.nombre_cliente)
        tipo_cliente = str(entidad.tipo_cliente)

        return ClienteDTO(fecha_creacion, fecha_actualizacion, _id, id_cliente, nombre_cliente=nombre_cliente, tipo_cliente=tipo_cliente)

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente = Cliente()
        cliente.id_cliente = dto.id_cliente
        cliente.nombre_cliente = dto.nombre_cliente
        cliente.tipo_cliente = dto.tipo_cliente
        return cliente

class MapeadorPropiedadDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO(id_propiedad=externo.get("propiedad_id"), nombre_propiedad=externo.get("nombre_propiedad"), estado_propiedad="LIBRE")
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__