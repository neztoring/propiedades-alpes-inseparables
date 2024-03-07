from src.bff_web.comandosIntegracion import ComandoIntegracion
import strawberry
import typing
import uuid

from strawberry.types import Info
from src.bff_web import utils
from src.bff_web.despachadores import Despachador

from .esquemas import *


@strawberry.type
class Mutation:


    @strawberry.mutation
    async def registrar_propiedad(self, id_propiedad: str, nombre_propiedad: str, estado_propiedad: str, cliente_propiedad: str, info: Info) -> PropiedadRespuesta:
        print(f"ID Propiedad: {id_propiedad}, Tipo Transaccion: {nombre_propiedad}")
        propiedadLoad = dict(
            id_propiedad = id_propiedad,
            nombre_propiedad = nombre_propiedad,
            estado_propiedad = estado_propiedad,
            cliente_propiedad = cliente_propiedad
        )

        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            #specversion = "v1",
            type = "ComandoCiente",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = propiedadLoad
        ) 

   
        print(f" ComandoIntegra*******: {comando}")
        despachador = Despachador()
        #info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-cliente", "public/default/comando-cliente")
        info.context["background_tasks"].add_task(despachador.publicar_comando, comando, "comandos-cliente")
        
        return PropiedadRespuesta(mensaje="Procesando Mensaje", codigo=203)



       