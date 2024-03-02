from src.propiedadesalpes.modulos.propiedad.dominio.entidades import Propiedad
from src.propiedadesalpes.seedwork.dominio.repositorios import Mapeador
from .dto import Propiedad as PropiedadDTO

class MapeadorPropiedad(Mapeador):

    def obtener_tipo(self) -> type:
        return Propiedad.__class__
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        propiedad_dto = PropiedadDTO()
        propiedad_dto.fecha_creacion = entidad.fecha_creacion
        propiedad_dto.fecha_actualizacion = entidad.fecha_actualizacion
        propiedad_dto.id = str(entidad.id)
        propiedad_dto.id_propiedad = str(entidad.id_propiedad)
        propiedad_dto.nombre_propiedad = str(entidad.nombre_propiedad)
        propiedad_dto.estado_propiedad = str(entidad.estado_propiedad)
        propiedad_dto.cliente_propiedad = str(entidad.cliente_propiedad)

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(
            dto.id, dto.fecha_creacion,
            dto.fecha_actualizacion, dto.id_propiedad,
            dto.nombre_propiedad, dto.estado_propiedad,
            dto.cliente_propiedad)
        propiedad.id_propiedad = dto.id_propiedad
        propiedad.nombre_propiedad = dto.nombre_propiedad
        propiedad.estado_propiedad = dto.estado_propiedad
        propiedad.cliente_propiedad = dto.cliente_propiedad
        return propiedad