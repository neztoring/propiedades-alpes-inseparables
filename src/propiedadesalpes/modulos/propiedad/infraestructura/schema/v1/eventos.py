from pulsar.schema import *
from src.propiedadesalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
import json

class EventoTransaccionCreadaPayload(Record):
    id_propiedad = String()
    fecha_creacion = Long()
    tipo_transaccion = String()

class EventoTransaccionCreada(EventoIntegracion):
    data = EventoTransaccionCreadaPayload()