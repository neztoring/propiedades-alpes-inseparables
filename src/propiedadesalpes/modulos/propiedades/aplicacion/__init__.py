from pydispatch import dispatcher

from .handlers import HandlerTransaccionIntegracion

from propiedadesalpes.modulos.propiedades.dominio.eventos import TransaccionCreada

dispatcher.connect(HandlerTransaccionIntegracion.handle_transaccion_creada, signal=f'{TransaccionCreada.__name__}Integracion')