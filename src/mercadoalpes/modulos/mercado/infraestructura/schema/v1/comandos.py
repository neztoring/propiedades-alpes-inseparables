from pulsar.schema import *
from dataclasses import dataclass, field
from src.mercadoalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearTransaccionPayload(ComandoIntegracion):
    id_propiedad = String()
    fecha_creacion = Long()


class ComandoCrearTransaccion(ComandoIntegracion):
    data = ComandoCrearTransaccionPayload()