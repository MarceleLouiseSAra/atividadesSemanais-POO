from abc import ABC, abstractmethod 

class interfaceCalendario(ABC):
    @abstractmethod
    def criaListaDeListas(self) -> list:
        pass

    @abstractmethod
    def retiraDias(self, mes : int, aux : list) -> list:
        pass

class interfaceFeriados(ABC):
    @abstractmethod
    def listaDeFeriados(self) -> list:
        pass

    @abstractmethod
    def removeFeriados(self, listaDeDias : list) -> list:
        pass

    @abstractmethod
    def removeFinsDeSemana(self, listaDeDias : list) -> list:
        pass

