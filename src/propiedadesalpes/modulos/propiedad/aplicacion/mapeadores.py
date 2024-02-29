from src.propiedadesalpes.seedwork.aplicacion.dto import DTO, Mapeador as AppMap
from src.propiedadesalpes.seedwork.aplicacion.dto import MapeadorList as AppMapList
from src.propiedadesalpes.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import PropiedadDTO
from src.propiedadesalpes.modulos.propiedad.dominio.entidades import Propiedad

class MapeadorListaPropiedadToJSON(AppMapList):
    def externos_a_dtos(self, externo: list) -> list[PropiedadDTO]:
        lista = []
        for record in externo:
            propiedad_dto = PropiedadDTO(
                id_propiedad=record.get("id_propiedad"),
                nombre_propiedad=record.get("nombre_propiedad"),
                estado_propiedad=record.get("estado_propiedad"),
                cliente_propiedad=record.get("cliente_propiedad")
            )
            lista.append(propiedad_dto)
        return lista
    
    def dtos_a_externos(self, dto: list[PropiedadDTO]) -> list:
        lista = []
        for record in dto:
            lista.append(record.__dict__)
        return lista
            

class MapeadorPropiedadDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO(
            id_propiedad=externo.get("id_propiedad"),
            nombre_propiedad=externo.get("nombre_propiedad"),
            estado_propiedad=externo.get("estado_propiedad"),
            cliente_propiedad=externo.get("cliente_propiedad")
        )
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        id_propiedad = str(entidad.id_propiedad)
        estado_propiedad = str(entidad.estado_propiedad)
        cliente_propiedad = str(entidad.cliente_propiedad)
        nombre_propiedad = str(entidad.nombre_propiedad)

        return PropiedadDTO(
            fecha_creacion=fecha_creacion, 
            fecha_actualizacion=fecha_actualizacion, 
            id=_id, 
            id_propiedad=id_propiedad,
            estado_propiedad=estado_propiedad,
            cliente_propiedad=cliente_propiedad,
            nombre_propiedad=nombre_propiedad)

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        propiedad.id_propiedad = dto.id_propiedad
        propiedad.estado_propiedad = dto.estado_propiedad
        propiedad.cliente_propiedad = dto.cliente_propiedad
        propiedad.nombre_propiedad = dto.nombre_propiedad
        return propiedad
