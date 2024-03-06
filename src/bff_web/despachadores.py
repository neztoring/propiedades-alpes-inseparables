import pulsar
from pulsar.schema import *
from .eventos import *

from . import utils

class Despachador:
    def __init__(self):
        ...


    async def publicar_evento(self, evento, topico):
        payload = EventoTransaccionCreadaPayload(
            id_propiedad=str(evento.data.id_propiedad),
            tipo_transaccion=str(evento.data.tipo_transaccion)
        )
        evento_integracion = EventoTransaccionCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoTransaccionCreada))



    async def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        print(f"===================== Mensaje publicado en [{topico}] =====================")
        cliente.close()


 