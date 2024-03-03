from pulsar.schema import *
from dataclasses import dataclass, field
from src.clientesalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearClientePayload(ComandoIntegracion):
    id_cliente = String()

class ComandoCrearCliente(ComandoIntegracion):
    data = ComandoCrearClientePayload()

class ComandoCreaPropiedadPayload(ComandoIntegracion):
    id_propiedad = String()
    nombre_propiedad = String()
    estado_propiedad = String()
    cliente_propiedad = String()


class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCreaPropiedadPayload()