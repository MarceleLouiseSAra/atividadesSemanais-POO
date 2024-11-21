from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, _nomeDoAnimal):
        self.Nome = _nomeDoAnimal

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, _nomeDoCachorro):
        super().__init__(_nomeDoCachorro)

    def emitir_som(self):
        return "Au au!"


class Gato(Animal):
    def __init__(self, _nomeDoGato):
        super().__init__(_nomeDoGato)

    def emitir_som(self):
        return "Miau!"
    
def main():
    Mingal = Gato("Mingal")
    print(Mingal.emitir_som())

    Floquinho = Cachorro("Floquinho")
    print(Floquinho.emitir_som())

main()
