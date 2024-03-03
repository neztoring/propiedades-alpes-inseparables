import pulsar
from pulsar.schema import *

from src.clientesalpes.modulos.cliente.infraestructura.schema.v1.eventos import EventoClienteCreada, EventoClienteCreadaPayload
from src.clientesalpes.modulos.cliente.infraestructura.schema.v1.comandos import ComandoCrearCliente, ComandoCrearClientePayload, ComandoCrearPropiedad, ComandoCreaPropiedadPayload
from src.clientesalpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoCrearPropiedad))
        publicador.send(mensaje)
        cliente.close()

    #Por ahora no es necesario que este servicio publique eventos, solamente comandos
    """
    def publicar_evento(self, evento, topico):
        payload = EventoClienteCreada(
            id_cliente=str(evento.id_cliente),
            fecha_creacion=str(evento.fecha_creacion)
        )
        evento_integracion = EventoClienteCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoClienteCreada))"""

    def publicar_comando(self, comando, topico):
        payload = ComandoCreaPropiedadPayload(
            id_propiedad = str(comando.id_propiedad),
            nombre_propiedad = str(comando.nombre_propiedad),
            estado_propiedad = str(comando.estado_propiedad),
            cliente_propiedad = str(comando.cliente_propiedad)
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))
        print(f"===================== Comando publicado en [{topico}] =====================")