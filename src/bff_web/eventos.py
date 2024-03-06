from pulsar.schema import *
from src.mercadoalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
import json
from mensajes import *

class EventoTransaccionCreadaPayload(Record):
    id_propiedad = String()
    fecha_creacion = Long()
    tipo_transaccion = String()

class EventoTransaccionCreada(EventoIntegracion):
    data = EventoTransaccionCreadaPayload()

class EventoIntegracion(Mensaje):
    ...