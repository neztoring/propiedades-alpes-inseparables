import pulsar
from pulsar.schema import *
#from .eventos import *
from .comandos  import *

from . import utils

class Despachador:
    def __init__(self):
        ...


    """ async def publicar_evento(self, evento, topico):
        evento_integracion = EventoTransaccionCreada(data=evento)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoTransaccionCreada))



    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        print(f"===================== Mensaje publicado en [{topico}] =====================")
        cliente.close() """

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoCrearPropiedad))
        publicador.send(mensaje)
        cliente.close()



    def publicar_comando(self, comando, topico):
        """ payload = ComandoCreaPropiedadPayload(
            id_propiedad = str(comando.id_propiedad),
            nombre_propiedad = str(comando.nombre_propiedad),
            estado_propiedad = str(comando.estado_propiedad),
            cliente_propiedad = str(comando.cliente_propiedad)
        )
        comando_integracion = ComandoCrearPropiedad(data=payload) """
        self._publicar_mensaje(comando, topico, AvroSchema(ComandoCrearPropiedad))
        print(f"===================== Comando publicado en [{topico}] =====================")

    async def publicar_mensaje(self, mensaje, topico, schema):
        json_schema = utils.consultar_schema_registry(schema)  
        avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)

        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=avro_schema)
        publicador.send(mensaje)
        cliente.close()


 