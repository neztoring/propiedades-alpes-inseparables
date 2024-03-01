from src.clientesalpes.seedwork.dominio.reglas import ReglaNegocio

class TieneCliente(ReglaNegocio):

    cliente: str = None
    
    def __init__(self, cliente, mensaje='Debe exisitir un cliente en la transaccion'):
        super().__init__(mensaje)
        self.cliente = cliente

    def es_valido(self) -> bool:
        return self.cliente is not None 