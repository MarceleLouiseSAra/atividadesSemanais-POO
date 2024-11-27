from feriados import feriados
from calendario import calendario

def verificaEntradaNumerica(x):

    while True:
        try:
            entrada = int(input(""))
        except(ValueError, TypeError):
            print("\nEntrada inválida: o tipo da entrada não é o esperado. Forneça uma nova entrada.")
            continue
        except Exception as erro:
            print(f"\nEntrada inválida: foi encontrado um erro do tipo {erro().__class__}")
            continue
        else:
            if entrada < 0:
                print("A entrada fornecida ou é menor que zero ou maior do doze; forneça uma entrada válida.")
                continue
            elif x == 1:
                if entrada > 2050 or entrada < 2010:
                    print("Forneça como entrada um ano entre 2010 e 2050.")
                else:
                    return entrada
            elif x == 2:
                if entrada < 1 or entrada > 12:
                    print("Forneça como entrada um mês entre janeiro (1) e dezembro (12).")
                else:
                    return entrada
            else:
                return entrada


def main():

    print("\nOlá!, vamos calcular quanto tempo você terá para fazer o projeto final de P.O.O.?")

    print("\nEm que ano você está?: ")
    ano = verificaEntradaNumerica(1)

    print("\nEm que mês começa o seu semestre?: ")
    inicio = verificaEntradaNumerica(2)

    print("\nEm que mês ele acaba?: ")
    fim = verificaEntradaNumerica(2)

    print("\nDe quantas hora por dia você dispõe para se dedicar ao trabalho?: ", end = "\n")
    horas = verificaEntradaNumerica(0)

    objFeriados = feriados(ano, inicio, fim)

    objCalendario = calendario(ano, inicio, fim)
    objCalendario.criaListaDeListas()

    print("Lista de dias com feriados e fins de semana: ", end = "\n\n")
    print(objCalendario.listaDeListas, end = "\n\n")
    print("Número de dias: ", len(objCalendario.listaDeListas), end = "\n\n")

    objCalendario.listaDeListas = objFeriados.removeFinsDeSemana(objCalendario.listaDeListas)
    objCalendario.listaDeListas = objFeriados.removeFeriados(objCalendario.listaDeListas)
    
    print("Lista de dias sem feriados e fins de semana: ", end = "\n\n")
    print(objCalendario.listaDeListas, end = "\n\n")
    print("Número de dias: ", len(objCalendario.listaDeListas), end = "\n\n")

    print(f"\nVocê tem {len(objCalendario.listaDeListas)*horas} horas para realizar o trabalho final de P.O.O.")

main()