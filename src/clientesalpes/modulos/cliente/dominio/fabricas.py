from .entidades import Cliente
from .reglas import TieneCliente
from .excepciones import TipoObjetoNoExisteEnDominioClientesExcepcion
from src.clientesalpes.seedwork.dominio.repositorios import Mapeador
from src.clientesalpes.seedwork.dominio.fabricas import Fabrica
from src.clientesalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaCliente(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            cliente: Cliente = mapeador.dto_a_entidad(obj)
            self.validar_regla(TieneCliente(cliente.id_cliente))
            
            return cliente

@dataclass
class FabricaHistorico(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Cliente.__class__:
            fabrica_cliente = _FabricaCliente()
            return fabrica_cliente.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioClientesExcepcion()