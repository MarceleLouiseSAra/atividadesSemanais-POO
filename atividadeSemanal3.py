class Musico:
    def __init__(self, _nomeDoMusico):
        self.nomeDoMusico = _nomeDoMusico

class Pianista(Musico):
    def tocar_instrumento(self):
        print(f"{self.nomeDoMusico} está tocando a nona sinfonia")

class Percussionista(Musico):
    def tocar_instrumento(self):
        print(f"{self.nomeDoMusico} está tocando percussão sempre no ritmo sincronizado")

def verificaEntrada(_nomeDoMusico):
    while True:

        _nomeDoMusico = input("\nQual o nome do músico? ")

        if not(_nomeDoMusico.isalpha()):
            for letra in range(len(_nomeDoMusico)):
                if _nomeDoMusico[letra].isspace() or _nomeDoMusico[letra].isalpha():
                    controle = 1
                    continue
                elif _nomeDoMusico[letra].isdigit():
                    print("Entrada inválida. Dê uma nova entrada:\n")
                    controle = 0
                    break
                else:
                    print("Entrada inválida. Dê uma nova entrada:\n")
                    controle = 0
                    break
        else:
            return _nomeDoMusico

        if controle:
            return _nomeDoMusico

def main():
    _nomeDoPianista = ""
    pianista0 = Pianista(verificaEntrada(_nomeDoPianista))
    pianista0.tocar_instrumento()

    _nomeDoPercussionista = ""
    percussionista0 = Percussionista(verificaEntrada(_nomeDoPercussionista))
    percussionista0.tocar_instrumento()

main()
