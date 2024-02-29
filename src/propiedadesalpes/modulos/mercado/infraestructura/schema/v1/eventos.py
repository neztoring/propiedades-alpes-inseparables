from pulsar.schema import *
from src.propiedadesalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
import json

class EventoTransaccionCreadaPayload(Record):
    id_propiedad = String()
    fecha_creacion = Long()
    tipo_transaccion = String()

class EventoTransaccionCreada(EventoIntegracion):
    data = EventoTransaccionCreadaPayload()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)