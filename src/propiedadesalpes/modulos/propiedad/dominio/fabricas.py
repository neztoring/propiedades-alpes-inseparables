from .entidades import Propiedad
from .reglas import TieneCliente
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from src.propiedadesalpes.seedwork.dominio.repositorios import Mapeador
from src.propiedadesalpes.seedwork.dominio.fabricas import Fabrica
from src.propiedadesalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)
            self.validar_regla(TieneCliente(propiedad.id_propiedad)) 
            
            return propiedad

@dataclass
class FabricaHistorico(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedad = FabricaPropiedad()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion() 