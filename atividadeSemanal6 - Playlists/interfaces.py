#interfaces.py

from abc import ABC, abstractmethod

class interfaceArtista(ABC):
    def  __init__(self) -> None:
        pass

    @abstractmethod
    def addMusica(self) -> None:
        pass

    @abstractmethod
    def setGeneroMusical(self) -> None:
        pass

class interfacePlaylist(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def addMusica(self) -> None:
        pass