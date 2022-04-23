from abc import ABC, abstractmethod

class ValidatorInterface(ABC):

    @abstractmethod
    def validate(self, moeda:str) -> bool:
        pass

    @abstractmethod
    def action(self) -> None:
        pass
    