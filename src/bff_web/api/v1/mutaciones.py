import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:


    @strawberry.mutation
    async def registrar_transaccion(self, id_propiedad: str, tipo_transaccion: str, info: Info) -> TransaccionRespuesta:
        print(f"ID Propiedad: {id_propiedad}, Tipo Transaccion: {tipo_transaccion}")
        transaccionload = dict(
            id_propiedad = id_propiedad,
            tipo_transaccion = tipo_transaccion,
            fecha_creacion = utils.time_millis()
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoTransaccion",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = transaccionload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_evento, comando, "eventos-mercado")
        
        return TransaccionRespuesta(mensaje="Procesando Mensaje", codigo=203)