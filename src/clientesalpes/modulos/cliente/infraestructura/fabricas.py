from dataclasses import dataclass, field
from src.clientesalpes.seedwork.dominio.fabricas import Fabrica
from src.clientesalpes.seedwork.dominio.repositorios import Repositorio
from src.clientesalpes.modulos.cliente.dominio.repositorios import RepositorioClientes
from .repositorios import RepositorioClientesSQLite
from .excepciones import ExcepcionFabrica, NoExisteImplementacionParaTipoFabricaExcepcion


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioClientes.__class__:
            return RepositorioClientesSQLite()
        else:
            raise NoExisteImplementacionParaTipoFabricaExcepcion()