import pulsar
from pulsar.schema import *

from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.eventos import EventoTransaccionCreada, EventoTransaccionCreadaPayload
from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.comandos import ComandoCrearTransaccion, ComandoCrearTransaccionPayload
from src.mercadoalpes.seedwork.infraestructura import utils

import datetime, json

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoTransaccionCreada))
        publicador.send(mensaje)
        print(f"===================== Mensaje publicado en [{topico}] =====================")
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = EventoTransaccionCreadaPayload(
            id_propiedad=str(evento.id_propiedad),
            tipo_transaccion=str(evento.tipo_transaccion)
        )
        evento_integracion = EventoTransaccionCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoTransaccionCreada))

     #Por ahora no es necesario que este servicio publique comandos, solamente eventos 
    """def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearTransaccionPayload(
            id_propiedad=str(comando.id_propiedad),
            tipo_transaccion=str(comando.tipo_transaccion)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearTransaccion(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearTransaccion))"""