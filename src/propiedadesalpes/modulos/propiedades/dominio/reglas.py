from src.propiedadesalpes.seedwork.dominio.reglas import ReglaNegocio

class TienePropiedad(ReglaNegocio):

    propiedad: str = None
    
    def __init__(self, propiedad, mensaje='Debe exisitir una propiedad en la transaccion'):
        super().__init__(mensaje)
        self.propiedad = propiedad

    def es_valido(self) -> bool:
        return self.propiedad is not None 