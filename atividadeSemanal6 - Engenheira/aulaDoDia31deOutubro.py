from abc import ABC, abstractmethod
import math

def verificaEntradaNumerica():
     while True:
         try:
             entradaNumerica = int(input())
         except (ValueError, TypeError):
             print("\nO tipo da entrada dada não é o esperado. Forneça outra entrada.")
         except Exception as erro:
             print(f"\nEntrada inválida: foi encontrado um {erro().__class__}. Forneça outra entrada.")
         else:
             if entradaNumerica < 0:
                 print("\nEntrada negativa. Forneça uma entrada positiva.")
             else:
                 return entradaNumerica

class formaGeometrica(ABC):
    def __init__(self, _numeroDeLados):
        self.numeroDeLados = _numeroDeLados
        self.vetorDeLados = []

    def le_lados(self):
        for lado in range(self.numeroDeLados):
            print("Lado ", lado+1, ": ")
            medida = verificaEntradaNumerica()
            self.vetorDeLados.append(medida)

    def mostra_lados(self):
        for lado in range(self.numeroDeLados):
            print("Lado ", lado+1, ": ", self.vetorDeLados[lado])

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Retangulo(formaGeometrica):
    def __init__(self, _numeroDeLados):
        super().__init__(_numeroDeLados)

    def calcular_area(self):
        result = 1
        for lado in range(len(self.vetorDeLados)):
            result *= self.vetorDeLados[lado]
            
        return result

    def calcular_perimetro(self):
        result = 0
        for lado in range(len(self.vetorDeLados)):
            result += self.vetorDeLados[lado]

        return result

class Quadrado(formaGeometrica):
    def __init__(self, _numeroDeLados):
        super().__init__(_numeroDeLados)

    def calcular_area(self):
        result = 1
        for lado in range(len(self.vetorDeLados)):
            result *= self.vetorDeLados[lado]
            
        return result

    def calcular_perimetro(self):
        result = 0
        for lado in range(len(self.vetorDeLados)):
            result += self.vetorDeLados[lado]

        return result

class Triangulo(formaGeometrica):
    def __init__(self, _numeroDeLados):
        super().__init__(_numeroDeLados)

    def calcular_area(self):
        s = 0
        for lado in range(len(self.vetorDeLados)):
            s += self.vetorDeLados[lado]

        s = s/2

        return math.sqrt(s * (s - self.vetorDeLados[0]) * (s - self.vetorDeLados[1]) * (s - self.vetorDeLados[2]))

    def calcular_perimetro(self):
        result = 0
        for lado in range(len(self.vetorDeLados)):
            result += self.vetorDeLados[lado]

        return result

def switch(match):

    match match:
        case 1:
            print("\nEsta figura é um quadrado!")
            forma0 = Quadrado(4)
            print("\nQuanto mede o lado desse quadrado?: ")

            while True:

                forma0.le_lados()
                
                for lado in range(len(forma0.vetorDeLados)):
                    if lado == 0:
                        continue
                    else:
                        if forma0.vetorDeLados[lado] != forma0.vetorDeLados[lado-1]:
                            print("\nOs lados do quadrado precisam ter a mesma medida!")
                            forma0.vetorDeLados.clear()
                            controle = 0
                            break
                        else:
                            controle = 1
                            break
                if controle:
                    break

            print("\nOs lados dessa figura são: ")
            forma0.mostra_lados()

            print("\nEssa figura tem área igual a ", forma0.calcular_area())
            print("\nEssa figura tem perímetro igual a ", forma0.calcular_perimetro())

        case 2:
            print("\nEsta figura é um retângulo!")
            forma0 = Retangulo(4)
            print("\nQuanto medem os lados desse retângulo?: ")

            while True:

                forma0.le_lados()
                
                for lado in range(len(forma0.vetorDeLados)):
                    if forma0.vetorDeLados[0] != forma0.vetorDeLados[1] or forma0.vetorDeLados[2] != forma0.vetorDeLados[3]:
                        print("\nO retângulo precisa ter dois pares de lados iguais.")
                        forma0.vetorDeLados.clear()
                        controle = 0
                        break
                    else:
                        controle = 1
                        break

                if controle:
                    break


            print("\nOs lados dessa figura são: ")
            forma0.mostra_lados()

            print("\nEssa figura tem área igual a ", forma0.calcular_area())
            print("\nEssa figura tem perímetro igual a ", forma0.calcular_perimetro())

        case 3:
            print("\nEsta figura é um triângulo!")
            forma0 = Triangulo(3)

            print("\nQuanto mede cada lado desse retângulo?: ")
            forma0.le_lados()

            print("\nOs lados dessa figura são:")
            forma0.mostra_lados()

            print("\nEssa figura tem área igual a ", forma0.calcular_area())
            print("\nEssa figura tem perímetro igual a ", forma0.calcular_perimetro())

        case _:
            print("\nEsta não é uma opção: escolha entre as opções 1, 2 e 3.")

def main():
    
    print("\nEscolha entre as opções 1, 2 e 3.")
    switch(verificaEntradaNumerica())

main()