#Formas.py

from Interface import interfaceFormas

def verificaEntradaNumerica():
     while True:
         try:
             entradaNumerica = int(input("Quanto mede o lado?: "))
         except (ValueError, TypeError):
             print("\nO tipo da entrada dada não é o esperado. Forneça outra entrada.")
         except Exception as erro:
             print(f"\nEntrada inválida: foi encontrado um {erro().__class__}. Forneça outra entrada.")
         else:
             if entradaNumerica < 0:
                 print("\nEntrada negativa. Forneça uma entrada positiva.")
             else:
                 return entradaNumerica

class Retangulo(interfaceFormas):
    def __init__(self) -> None:
        self.numeroDeLados = 2
        self.ladoMaior = verificaEntradaNumerica()
        self.ladoMenor = verificaEntradaNumerica()

    def calcularArea(self) -> None:
        result = self.ladoMaior * self.ladoMenor
        print("A área deste retângulo é ", result, ".")

    def calcularPerimetro(self) -> None:
        result = 2*self.ladoMaior + 2*self.ladoMenor
        print("O perímetro deste retângulo é ", result, ".")
    
class Quadrado(interfaceFormas):
    def __init__(self) -> None:
        self.ladosDoQuadrado = verificaEntradaNumerica()

    def calcularArea(self) -> None:
        result = 2 * self.ladosDoQuadrado
        print("A área deste quadrado é ", result, ".")

    def calcularPerimetro(self) -> None:
        result = 4 * self.ladosDoQuadrado
        print("O perímetro deste quadrado é ", result, ".")