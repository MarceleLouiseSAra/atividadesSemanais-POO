class Cliente:
    def __init__(self, _nomeDoCliente, _diasEstadia, _consumoRestaurante):
        self.Nome = _nomeDoCliente
        self.diasEstadia = _diasEstadia
        self.consumoRestaurante = _consumoRestaurante

def fornecaValorConta(self, objetoHotel):
    objetoHotel.determineContaCliente(self)

class Hotel:
    def __init__(self, _nomeDoHotel):
        self.nomeHotel = _nomeDoHotel

def determineContaCliente(self, objetoCliente):

    resultado = (objetoCliente.diasEstadia * 100) + (objetoCliente.consumoRestaurante * 50)
    print(f"\nO cliente {objetoCliente.Nome} que ficou {objetoCliente.diasEstadia} dias no hotel {self.nomeHotel} teve a conta de R$ {resultado},00 reais, considerando {objetoCliente.diasEstadia} dias de hospedagem e {objetoCliente.consumoRestaurante} refeições.\n")

def main():

    cliente0 = Cliente("Marcele", 5, 15)
    hotel0 = Hotel("Cinco Estrelas")

    while True:
        nomeCliente = input("\nQual o nome do cliente? ")
        if nomeCliente.isalpha():
            break
        else:
            print("Entrada inválida. Dê uma nova entrada:\n")
            continue

    while True:
        diasEstadia = input("\nQuanto tempo ele ficou hospedado? ")
        if diasEstadia.isdigit():
            diasEstadia = int(diasEstadia)
            if diasEstadia < 0:
                print("Entrada negativa. Dê uma nova entrada:\n")
                continue
            else:
                break
        else:
            print("Entrada inválida. Dê uma nova entrada:\n")
            continue

    while True:
        consumoRestaurante = input("\nQuantas refeições ele fez no restaurante? ")
        if consumoRestaurante.isdigit():
            consumoRestaurante = int(consumoRestaurante)
            if consumoRestaurante < 0:
                print("Entrada negativa. Dê uma nova entrada:\n")
                continue
            else:
                break
        else:
            print("Entrada inválida. Dê uma nova entrada:\n")
        continue

    cliente0 = Cliente(nomeCliente, diasEstadia, consumoRestaurante)

    while True:

        nomeHotel = input("\nQual o nome do hotel? ")

        if not(nomeHotel.isalnum()):
            for letra in range(len(nomeHotel)):
                if nomeHotel[letra].isspace():
                    controle = 1
                    continue
                elif nomeHotel[letra].isalnum():
                    controle = 1
                    continue
                else:
                    print("Entrada inválida. Dê uma nova entrada:\n")
                    controle = 0
                    break
        else:
            break

        if controle:
            break

    hotel0 = Hotel(nomeHotel)

    cliente0.fornecaValorConta(hotel0)

main()