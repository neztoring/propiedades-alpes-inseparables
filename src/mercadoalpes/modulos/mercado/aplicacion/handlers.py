from src.propiedadesalpes.seedwork.aplicacion.handlers import Handler
from src.propiedadesalpes.modulos.mercado.infraestructura.despachadores import Despachador

class HandlerTransaccionIntegracion(Handler):

    @staticmethod
    def handle_transaccion_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-transaccion')


    