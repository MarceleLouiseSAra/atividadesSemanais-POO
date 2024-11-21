#Interfaces.py

from abc import ABC, abstractmethod

class interfaceFormas(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass