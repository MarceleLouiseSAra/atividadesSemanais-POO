def verificaEntradaAlfabetica():

    while True:

        entradaAlfabetica = input("\n")

        if (entradaAlfabetica.isalpha()):

            for letra in range(len(entradaAlfabetica)):
                if entradaAlfabetica[letra].isalpha():
                    controle = 1
                    continue
                else:
                    controle = 0
                    print("\nEntrda inválida. Forneça uma nova entrada.")
                    break
        else:
            return entradaAlfabetica
        
        if controle:
            return entradaAlfabetica
        else:
            continue

cerveja = {
    "nome": "cerveja",
    "alcoolica": True
}

cachaçaCoquinho = {
    "nome": "cachaça coquinho",
    "alcoolica": True
}

vinho = {
    "nome": "vinho",
    "alcoolica": True
}

toddynho = {
    "nome": "toddynho",
    "alcoolica": False
}

sucoDeLaranja = {
    "nome": "suco de laranja",
    "alcoolica": False
}

agua = {
    "nome": "agua",
    "alcoolica": False
}

bebidas = [cerveja, cachaçaCoquinho, vinho, toddynho, sucoDeLaranja, agua]

class Festeiro:
    def __init__(self, nome : str, cpf : str, cupomDeDesconto : str) -> None:
        self.nome = nome
        self.__cpf = cpf
        self._cupomDeDesconto = []
        self._cupomDeDesconto.append(cupomDeDesconto)

    @property
    def cpf(self) -> str: #mostra_cpf()
        return self.__cpf
    
    @property
    def cupomDeDesconto(self) -> str:
        return self._cupomDeDesconto
    
    @cpf.setter
    def cpf(self, cpf : str) -> None:
        self.__cpf = cpf

    @cupomDeDesconto.setter
    def cupomDeDesconto(self, cupomDeDesconto : str) -> None:
        self._cupomDeDesconto.append(cupomDeDesconto)


    def pedir_bebida(self) -> None:
        print("\nDe qual bebida você gostaria?", end = ": ")

        loop = 1
        for bebida in bebidas:
            print(bebida['nome'], end = "")
            if(loop == len(bebidas)-1):
                print(" ou ", end = "")
            elif(loop == len(bebidas)):
                print("?", end = "")
            else:
                print(", ", end = "")
            loop += 1
        
        entrada = verificaEntradaAlfabetica()

        for bebida in bebidas:
            if bebida.get('nome') == entrada:
                controle = 1
                if bebida.get('alcoolica') == True:
                    print("\nVocê poderia nos mostrar o seu CPF, por favor?")
                    if(self.cpf == ""):
                        print("\nDesculpe: só vendemos bebidas alcóolicas mediante apresentação do CPF.")
                        break
                    else:
                        print(f"\n{self.cpf}")
                        print("\nAqui está a sua bebida!")
                        break
                else:
                    print("\nAqui está a sua bebida!")
                    break
            else:
                controle = 0

        if controle == 0:
            print("\nDesculpe: não vendemos essa bebida aqui")
                

    def tem_desconto(self) -> None:
        if len(self.cupomDeDesconto) == 0:
            print("\nVocê não possui cupons de desconto para utilizar.")
        else:
            print("\nVocê possui cupons de desconto para utilizar. Você gostaria de utilizar algum?, qual?: ", end = "")

            loop = 1
            for cupom in self.cupomDeDesconto:
                print(cupom, end = "")
                if(loop == len(self.cupomDeDesconto)-1):
                    print(" ou ", end = "")
                elif(loop == len(self.cupomDeDesconto)):
                    print("?", end = "")
                else:
                    print(", ", end = "")
                loop += 1

        entrada = verificaEntradaAlfabetica()

        for cupom in self.cupomDeDesconto:
            if entrada == cupom:
                controle = 1
                self.cupomDeDesconto.remove(cupom)
                print("\nCupom utilizado com sucesso.")
                break
            else:
                controle = 0
                continue

        if controle == 0:
            print("\nDesculpe, mas esse cupom não existe.")

def main():
    
    objeto0 = Festeiro("Marcele", "13909533598", 'PRIMEIRAVEZ')
    print(f"{objeto0.nome}, {objeto0.cpf}, {objeto0.cupomDeDesconto}")

    objeto0.cpf = "12345678998"
    print(f"{objeto0.nome}, {objeto0.cpf}, {objeto0.cupomDeDesconto}")

    objeto0.cupomDeDesconto = "BEMVINDODEVOLTA"
    print(f"{objeto0.nome}, {objeto0.cpf}, {objeto0.cupomDeDesconto}")

    objeto0.pedir_bebida()

    objeto0.cpf = ""
    objeto0.pedir_bebida()

    objeto0.tem_desconto()

    print(f"{objeto0.cupomDeDesconto}")

main()