import pulsar
from pulsar.schema import *

from src.clientesalpes.modulos.cliente.infraestructura.schema.v1.eventos import EventoClienteCreada, EventoClienteCreadaPayload
from src.clientesalpes.modulos.cliente.infraestructura.schema.v1.comandos import ComandoCrearCliente, ComandoCrearClientePayload
from src.clientesalpes.seedwork.infraestructura import utils

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
        payload = EventoClienteCreadaPayload(
            id_cliente=str(evento.id_cliente),
            fecha_creacion=int(unix_time_millis(evento.fecha_evento))
        )
        evento_integracion = EventoClienteCreada(data=payload)
        self._publicar_mensaje(evento_integracion.toJSON(), topico)        