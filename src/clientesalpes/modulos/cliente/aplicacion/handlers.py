from src.clientesalpes.seedwork.aplicacion.handlers import Handler
from src.clientesalpes.modulos.cliente.infraestructura.despachadores import Despachador

class HandlerClienteIntegracion(Handler):

    @staticmethod
    def handle_crear_propiedad(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-cliente')


    