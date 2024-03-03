from dataclasses import dataclass, field
from .mixins import ValidarReglasMixin
from .reglas import IdEntidadEsInmutable
from .excepciones import IdDebeSerInmutableExcepcion
from datetime import datetime
import uuid
from .eventos import EventoDominio
from .comandos import ComandoDominio

@dataclass
class Entidad:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    fecha_creacion: datetime =  field(default=datetime.now())
    fecha_actualizacion: datetime = field(default=datetime.now())

    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not IdEntidadEsInmutable(self).es_valido():
            raise IdDebeSerInmutableExcepcion()
        self._id = self.siguiente_id()
        

@dataclass
class AgregacionRaiz(Entidad, ValidarReglasMixin):
    eventos: list[EventoDominio] = field(default_factory=list)
    comandos: list[ComandoDominio] = field(default_factory=list)

    def agregar_evento(self, evento: EventoDominio):
        self.eventos.append(evento)
    
    def limpiar_eventos(self):
        self.eventos = list()
    
    def agregar_comando(self, comando: ComandoDominio):
        self.comandos.append(comando)
    
    def limpiar_comandos(self):
        self.comandos = list()


@dataclass
class Locacion(Entidad):
    def __str__(self) -> str:
        ...