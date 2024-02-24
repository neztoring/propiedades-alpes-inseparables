from dataclasses import dataclass, field
from propiedadesalpes.seedwork.dominio.fabricas import Fabrica
from propiedadesalpes.seedwork.dominio.repositorios import Repositorio
from propiedadesalpes.modulos.propiedades.dominio.repositorios import RepositorioTransacciones
from .repositorios import RepositorioTransaccionesSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioTransacciones.__class__:
            return RepositorioTransaccionesSQLite()
        else:
            raise NoExisteImplementacionParaTipoFabricaExcepcion()