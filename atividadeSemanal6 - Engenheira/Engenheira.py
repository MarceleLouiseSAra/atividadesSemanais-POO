#Engenheira.py

from typing import Type
from Interfaces import interfaceFormas

class Engenheira:
    def __init__(self, _nome : str) -> None:
        self.nome = _nome

    def medirArea(self, terreno: Type[interfaceFormas]) -> None: #"terreno" já é um objeto da classe "interfaceFormas"
        terreno0 = terreno
        terreno0.calcularArea()

    def medirPerimetro(self, terreno: Type[interfaceFormas]) -> None:
        terreno0 = terreno
        terreno0.calcularPerimetro()