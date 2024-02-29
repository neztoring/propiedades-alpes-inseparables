from dataclasses import dataclass, field
from src.propiedadesalpes.seedwork.dominio.fabricas import Fabrica
from src.propiedadesalpes.seedwork.dominio.repositorios import Repositorio
from src.propiedadesalpes.modulos.propiedad.dominio.repositorios import RepositorioPropiedades
from .repositorios import RepositorioPropiedadesSQLite
from .excepciones import ExcepcionFabrica, NoExisteImplementacionParaTipoFabricaExcepcion


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesSQLite()
        else:
            raise NoExisteImplementacionParaTipoFabricaExcepcion()