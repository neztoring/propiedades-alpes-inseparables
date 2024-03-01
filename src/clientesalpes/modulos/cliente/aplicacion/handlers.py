from src.clientesalpes.seedwork.aplicacion.handlers import Handler
from src.clientesalpes.modulos.cliente.infraestructura.despachadores import Despachador

class HandlerClienteIntegracion(Handler):

    @staticmethod
    def handle_cliente_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')


    