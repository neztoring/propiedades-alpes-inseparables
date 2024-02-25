from pulsar.schema import *
from propiedadesalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class EventoTransaccionCreadaPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoTransaccionCreada(EventoIntegracion):
    data = EventoTransaccionCreadaPayload()