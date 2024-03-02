from pulsar.schema import *
from dataclasses import dataclass, field
from src.clientesalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearClientePayload(ComandoIntegracion):
    id_cliente = String()


class ComandoCrearCliente(ComandoIntegracion):
    data = ComandoCrearClientePayload()