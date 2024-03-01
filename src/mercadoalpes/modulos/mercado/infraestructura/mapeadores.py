from src.mercadoalpes.modulos.mercado.dominio.entidades import Transaccion
from src.mercadoalpes.seedwork.dominio.repositorios import Mapeador
from .dto import Transaccion as TransaccionDTO

class MapeadorTransaccion(Mapeador):

    def obtener_tipo(self) -> type:
        return Transaccion.__class__
    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        
        transaccion_dto = TransaccionDTO()
        transaccion_dto.fecha_creacion = entidad.fecha_creacion
        transaccion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        transaccion_dto.id = str(entidad.id)
        transaccion_dto.id_propiedad = str(entidad.id_propiedad)

        return transaccion_dto

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion(dto.id, dto.fecha_creacion, dto.fecha_actualizacion, dto.id_propiedad)
        transaccion.id_propiedad = dto.id_propiedad
        return transaccion