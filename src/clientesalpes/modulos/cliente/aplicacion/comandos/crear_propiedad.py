from src.clientesalpes.seedwork.aplicacion.comandos import Comando
from src.clientesalpes.modulos.cliente.aplicacion.dto import PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass
from src.clientesalpes.seedwork.aplicacion.comandos import ejecutar_comando as comando
from pydispatch import dispatcher

@dataclass
class CrearPropiedad(Comando):
    cliente_propiedad: str
    nombre_propiedad: str
    estado_propiedad: str
    id_propiedad: str

class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
            id_propiedad=comando.id_propiedad,
            nombre_propiedad=comando.nombre_propiedad,
            estado_propiedad=comando.estado_propiedad,
            cliente_propiedad=comando.cliente_propiedad
        )

        dispatcher.send(signal=f'{CrearPropiedad.__name__}Integracion', comando=propiedad_dto)

@comando.register
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando=comando)