from abc import ABC, abstractmethod

class AbstractPessoa(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def nome(self) -> str:
        pass

    @property
    @abstractmethod
    def celular(self) -> str:
        pass

    @property
    @abstractmethod
    def cpf(self) -> str:
        pass