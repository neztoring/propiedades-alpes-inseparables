from src.clientesalpes.seedwork.aplicacion.handlers import Handler
from src.clientesalpes.modulos.cliente.infraestructura.despachadores import Despachador

class HandlerClienteIntegracion(Handler):

    """@staticmethod
    def handle_cliente_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')"""
    
    @staticmethod
    def handle_crear_propiedad(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-cliente')


    