from pulsar.schema import *
from dataclasses import dataclass, field
from src.propiedadesalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    id_propiedad = String()
    nombre_propiedad = String()
    estado_propiedad = String()
    cliente_propiedad = String()


class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()