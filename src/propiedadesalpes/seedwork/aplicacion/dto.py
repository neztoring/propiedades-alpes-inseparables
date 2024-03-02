from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class DTO():
    ...

class Mapeador(ABC):
    @abstractmethod
    def externo_a_dto(self, externo: any) -> DTO:
        ...

    @abstractmethod
    def dto_a_externo(self, dto: DTO) -> any:
        ...

class MapeadorList(ABC):
    @abstractmethod
    def externos_a_dtos(self, externo: list) -> list[DTO]:
        ...

    @abstractmethod
    def dtos_a_externos(self, dto: list[DTO]) -> list:
        ...