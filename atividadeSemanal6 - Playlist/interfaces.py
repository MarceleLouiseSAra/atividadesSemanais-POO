#interfaces.py

from abc import ABC, abstractmethod

class interfaceManipularDados(ABC):

    @abstractmethod
    def loadJSon(self) -> None:
        pass

    @abstractmethod
    def writeJSon(self) -> None:
        pass

class interfaceArtista(ABC): #perguntar pra gabriela se eu posso fazer o construtor na interface
    def __init__(self, nome : str, generoMusical : str) -> None:
        pass

    @abstractmethod
    def addMusica(self) -> None:
        pass

    @abstractmethod
    def setGeneroMusical(self) -> None:
        pass

class interfacePlaylist(ABC):
    def __init__(self, nome : str) -> None:
        pass

    @abstractmethod
    def addMusica(self) -> None:
        pass