from .dto import TransaccionDTO
from src.propiedadesalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from src.propiedadesalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from src.propiedadesalpes.modulos.mercado.dominio.entidades import Transaccion

from datetime import datetime


class MapeadorTransaccionDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> TransaccionDTO:
        transaccion_dto = TransaccionDTO(id_propiedad=externo.get("id_propiedad"),tipo_transaccion=externo.get("tipo_transaccion"))
        return transaccion_dto

    def dto_a_externo(self, dto: TransaccionDTO) -> dict:
        return dto.__dict__


class MapeadorTransaccion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Transaccion.__class__

    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        id_propiedad = str(entidad.id_propiedad)
        tipo_transaccion = entidad.tipo_transaccion
        
        return TransaccionDTO(fecha_creacion, fecha_actualizacion, _id, id_propiedad,tipo_transaccion)

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion()
        transaccion.id_propiedad = dto.id_propiedad
        transaccion.tipo_transaccion=dto.tipo_transaccion
        return transaccion
