from src.propiedadesalpes.seedwork.aplicacion.comandos import Comando
from src.propiedadesalpes.modulos.mercado.aplicacion.dto import TransaccionDTO
from .base import CrearTransaccionBaseHandler
from dataclasses import dataclass
from src.propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_comando as comando
from src.propiedadesalpes.modulos.mercado.dominio.entidades import Transaccion
from src.propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.propiedadesalpes.modulos.mercado.aplicacion.mapeadores import MapeadorTransaccion
from src.propiedadesalpes.modulos.mercado.infraestructura.repositorios import RepositorioTransacciones

@dataclass
class CrearTransaccion(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    id_propiedad: str
    tipo_transaccion: str
    

class CrearTransaccionHandler(CrearTransaccionBaseHandler):
    def handle(self, comando: CrearTransaccion):
        transaccion_dto = TransaccionDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            id_propiedad=comando.id_propiedad,
            tipo_transaccion=comando.tipo_transaccion,

        )

        transaccion: Transaccion = self._fabrica_transacciones.crear_objeto(transaccion_dto, MapeadorTransaccion())
        transaccion.crear_transaccion(transaccion)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, transaccion)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register
def ejecutar_comando_crear_transaccion(comando: CrearTransaccion):
    handler = CrearTransaccionHandler()
    handler.handle(comando=comando)