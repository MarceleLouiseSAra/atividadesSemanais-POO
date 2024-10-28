def validaEntradaAlfabetica():
    while True:

        entradaAlfabetica = input("\nDê uma entrada alfabética: ")

        if not(entradaAlfabetica.isalpha()):
            for letra in range(len(entradaAlfabetica)):
                if entradaAlfabetica[letra].isalpha() or entradaAlfabetica[letra].isspace():
                    controle = 1
                    continue
                else:
                    print("\nEntrada inválida. Forneça uma nova entrada.")
                    controle = 0
                    break
        else:
            break

        if controle:
            break
        else:
            continue

def validaEntradaNumerica():

    while True:

        try:
            entradaNumerica = int(input("\nDê uma entrada numérica: "))
        except (ValueError, TypeError):
            print("\nEntrada inválida: o tipo da entrada não é o esperado. Forneça uma nova entrada.")
            continue
        except Exception as erro:
            print(f"\nEntrada inválida: foi encontrado um erro do tipo {erro().__class__}")
            continue
        else:
            if entradaNumerica < 0:
                print("\nEntrada negativa. Forneça uma entrada positiva.")
                continue
            else:
                break

def main():

    validaEntradaAlfabetica()
    validaEntradaNumerica()

main()
