from src.propiedadesalpes.seedwork.aplicacion.comandos import Comando
from src.propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_comando as comando
from src.propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from src.propiedadesalpes.modulos.propiedad.aplicacion.dto import PropiedadDTO
from src.propiedadesalpes.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedad
from src.propiedadesalpes.modulos.propiedad.dominio.entidades import Propiedad
from src.propiedadesalpes.modulos.propiedad.infraestructura.repositorios import RepositorioPropiedades

from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass

@dataclass
class CrearPropiedad(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    id_propiedad: str
    nombre_propiedad: str
    estado_propiedad: str
    cliente_propiedad: str

class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            id_propiedad=comando.id_propiedad,
            nombre_propiedad=comando.nombre_propiedad,
            estado_propiedad=comando.estado_propiedad,
            cliente_propiedad=comando.cliente_propiedad
        )

        propiedad: Propiedad = self._fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando=comando)