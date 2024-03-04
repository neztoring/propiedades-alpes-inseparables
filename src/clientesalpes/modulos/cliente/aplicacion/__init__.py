from pydispatch import dispatcher

from .handlers import HandlerClienteIntegracion

from src.clientesalpes.modulos.cliente.dominio.eventos import ClienteCreada
from src.clientesalpes.modulos.cliente.dominio.comandos import CrearPropiedad

dispatcher.connect(HandlerClienteIntegracion.handle_crear_propiedad, signal=f'{CrearPropiedad.__name__}Integracion')