from pulsar.schema import *
from src.clientesalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
import json

class EventoClienteCreadaPayload(Record):
    id_cliente = String()
    fecha_creacion = Long()

class EventoClienteCreada(EventoIntegracion):
    data = EventoClienteCreadaPayload()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)