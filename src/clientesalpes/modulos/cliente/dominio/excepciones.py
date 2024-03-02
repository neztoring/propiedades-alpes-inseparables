from src.clientesalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioClientesExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)