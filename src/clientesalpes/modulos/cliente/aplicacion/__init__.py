from pydispatch import dispatcher

from .handlers import HandlerClienteIntegracion

from src.clientesalpes.modulos.cliente.dominio.eventos import ClienteCreada

dispatcher.connect(HandlerClienteIntegracion.handle_cliente_creada, signal=f'{ClienteCreada.__name__}Integracion')