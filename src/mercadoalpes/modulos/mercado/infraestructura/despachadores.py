import pulsar
from pulsar.schema import *

from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.eventos import EventoTransaccionCreada, EventoTransaccionCreadaPayload
from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.comandos import ComandoCrearTransaccion, ComandoCrearTransaccionPayload
from src.mercadoalpes.seedwork.infraestructura import utils

import datetime, pika, json

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico):
        connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        channel = connection.channel()
        channel.queue_declare(queue=topico)
        channel.basic_publish(exchange='',
                                routing_key=topico,
                                body=json.dumps(mensaje))
        print("========== Mensaje publicado ==========", flush=True)
        connection.close()

    def publicar_evento(self, evento, topico):
        payload = EventoTransaccionCreadaPayload(
            id_propiedad=str(evento.id_propiedad),
            fecha_creacion=int(unix_time_millis(evento.fecha_evento)),
            tipo_transaccion=evento.tipo_transaccion
        )
        evento_integracion = EventoTransaccionCreada(data=payload)
        self._publicar_mensaje(evento_integracion.toJSON(), topico)        