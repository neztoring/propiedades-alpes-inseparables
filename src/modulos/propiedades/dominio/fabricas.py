from .entidades import Transaccion
from .reglas import TienePropiedad
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from propiedadesalpes.seedwork.dominio.repositorios import Mapeador
from propiedadesalpes.seedwork.dominio.fabricas import Fabrica
from propiedadesalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaTransaccion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            transaccion: Transaccion = mapeador.dto_a_entidad(obj)

            self.validar_regla(TienePropiedad(transaccion.id_propiedad))
            
            return transaccion

@dataclass
class FabricaHistorico(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Transaccion.__class__:
            fabrica_transaccion = _FabricaTransaccion()
            return fabrica_transaccion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion()