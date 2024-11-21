from abc import ABC, abstractmethod
from datetime import date

def verificaEntradaAlfabética():

    while True:

        entradaAlfabetica = input("\nDê uma entrada alfabética: ")

        if not(entradaAlfabetica).isalpha():
            for letra in range(len(entradaAlfabetica)):
                if entradaAlfabetica[letra].isalpha() or entradaAlfabetica[letra].isspace() or entradaAlfabetica[letra].isnumeric() or entradaAlfabetica[letra] == "@" or entradaAlfabetica[letra] == ".":
                    controle = 1
                    continue
                else:
                    controle = 0
                    print("\nEntrada inválida. Forneça uma entrada alfabética.")
                    break
        else:
            return entradaAlfabetica

        if controle:
            return entradaAlfabetica
        else:
            continue

def verificaEntradaNumerica():
    while True:
        try:
            entradaNumerica = int(input("\nDê uma entrada numérica: "))
        except (ValueError, TypeError):
            print("\nEntrada inválida: tipo da entrada dada é inesperado. Forneça uma nova entrada.")
        except Exception as erro:
            print(f"\nEntrada inválida: foi encontrado um {erro().__class__}. Forneça uma nova entrada.")
        else:
            if entradaNumerica < 0:
                print("\nEntrada negativa. Forneça uma entrada positiva.")
            else:
                return entradaNumerica

def loadUsuarios(_listaDeUsuarios):
    with open("banco.txt", "r") as arquivo:
        for linha in arquivo:
            _listaDeUsuarios.append(linha)


class Usuario:

    @abstractmethod
    def cadastrar(self):
        pass

class usuarioComum(Usuario):
    def __init__(self):
        self.nome = verificaEntradaAlfabética()
        self.email = verificaEntradaAlfabética()

    def cadastrar(self):
        with open("banco.txt", "a") as arquivo:
            arquivo.write(self.nome)
            arquivo.write(" ")
            arquivo.write(self.email)
            arquivo.write("\n")

class usuarioAdministrador(usuarioComum):
    def __init__(self):
        super().__init__()
        self.nivelDeAcesso = verificaEntradaAlfabética()

    def cadastrar(self):
        with open("banco.txt", "a") as arquivo:
            arquivo.write(self.nome)
            arquivo.write(" ")
            arquivo.write(self.email)
            arquivo.write(" ")
            arquivo.write(self.nivelDeAcesso)
            arquivo.write("\n")

class metodoPagamento(ABC):
    
    def __init__(self, _pagamento):
        self.pagamento = _pagamento

    @abstractmethod
    def processarPagamento(self):
        pass

    def salvarPagamento(self, metodo):
        with open("pagamentos.txt", "a") as arquivo:
            arquivo.write(f"{date.today()} - Pagamento de R$ {self.pagamento:.2f} processado com {metodo}.\n")


class cartaoCredito(metodoPagamento):
    def __init__(self, _pagamento):
        super().__init__(_pagamento)

    def processarPagamento(self):
        print("\nPagamento por cartão de crédito processado com sucesso.")
        super().salvarPagamento("cartao de crédito")

class payPal(metodoPagamento):
    def __init__(self, _pagamento):
        super().__init__(_pagamento)

    def processarPagamento(self):
        print("\nPagamento com PayPal processado com sucesso.")
        super().salvarPagamento("PayPal")

class transferenciaBancaria(metodoPagamento):
    def __init__(self, _pagamento):
        super().__init__(_pagamento)

    def processarPagamento(self):
        print("\nPagamento por transfrência bancária processado com sucesso.")
        super().salvarPagamento("transferência bancária")

def main():
    objeto0 = usuarioComum()
    objeto0.cadastrar()

    objeto1 = usuarioAdministrador()
    objeto1.cadastrar()

    listaDeUsuarios = []
    loadUsuarios(listaDeUsuarios)
    print(listaDeUsuarios)

    _pagamento = verificaEntradaNumerica()
    objeto2 = transferenciaBancaria(_pagamento)
    objeto2.processarPagamento()

    _pagamento = verificaEntradaNumerica()
    objeto3 = cartaoCredito(_pagamento)
    objeto3.processarPagamento()

    _pagamento = verificaEntradaNumerica()
    objeto4 = payPal(_pagamento)
    objeto4.processarPagamento()

main()