import pika, json

from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.eventos import EventoTransaccionCreada
from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.comandos import ComandoCrearTransaccion
from src.mercadoalpes.seedwork.infraestructura import utils

class PikaMassenger():
    topico : str = ""

    def __init__(self, topico, *args, **kwargs):
        self.topico = topico
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        self.channel = self.conn.channel()
        self.channel.queue_declare(queue=self.topico)

    def consume(self, keys, callback):
        self.channel.basic_consume(
            queue=self.topico, 
            on_message_callback=callback, 
            auto_ack=True)
        print('********** Esperando mensajes **********', flush=True)
        self.channel.start_consuming()


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

def suscribirse_a_eventos(topico):
    def callback(ch, method, properties, body):
        print("========== Mensaje recibido ==========", flush=True)
        body_decoded = body.decode("utf-8")
        body_json = json.loads(body_decoded)
        print(body_json)

    with PikaMassenger(topico) as consumer:
        consumer.consume(keys=[...], callback=callback)
