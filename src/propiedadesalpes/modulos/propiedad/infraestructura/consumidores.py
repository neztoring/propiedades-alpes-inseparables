import pulsar,_pulsar
from pulsar.schema import *
import logging
import traceback

from datetime import datetime

from src.propiedadesalpes.api import app

from src.propiedadesalpes.modulos.propiedad.aplicacion import dto
from src.propiedadesalpes.modulos.propiedad.aplicacion.servicios import ServicioPropiedad

from src.propiedadesalpes.modulos.propiedad.infraestructura.schema.v1.eventos import EventoTransaccionCreada
from src.propiedadesalpes.modulos.propiedad.infraestructura.schema.v1.comandos import ComandoCrearPropiedad


from src.propiedadesalpes.seedwork.infraestructura import utils

_FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-mercado', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-eventos',
                                       schema=AvroSchema(EventoTransaccionCreada))

        while True:
            mensaje = consumidor.receive()
            propiedad_mensaje = mensaje.value().data
            print(f'Evento recibido: {propiedad_mensaje}')

            with app.app_context():
                servicio_propiedad = ServicioPropiedad()
                propiedad_guardada = servicio_propiedad.obtener_propiedad_por_id(propiedad_mensaje.id_propiedad)
                
                servicio_propiedad.actualizar_estado_propiedad(propiedad_guardada, propiedad_mensaje.tipo_transaccion)
            

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-cliente', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-comandos',
                                       schema=AvroSchema(ComandoCrearPropiedad))

        while True:
            mensaje = consumidor.receive()
            propiedad_mensaje = mensaje.value().data
            print(f'Comando recibido: {propiedad_mensaje}')

            propiedad_dto = dto.PropiedadDTO(
                cliente_propiedad=propiedad_mensaje.cliente_propiedad, 
                nombre_propiedad=propiedad_mensaje.nombre_propiedad, 
                estado_propiedad=propiedad_mensaje.estado_propiedad, 
                id_propiedad=propiedad_mensaje.id_propiedad,
                fecha_actualizacion=datetime.today().strftime(_FORMATO_FECHA),
                fecha_creacion=datetime.today().strftime(_FORMATO_FECHA),
                id=propiedad_mensaje.id_propiedad
            )
            with app.app_context():
                servicio_propiedad = ServicioPropiedad()
                servicio_propiedad.crear_propiedad(propiedad_dto)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()