#Artista.py

from interfaces import interfaceArtista

def verificaEntrada() -> str:
    
    while True:

        entrada = input("\n")

        if not(entrada.isalpha()):

            for caractere in range(len(entrada)):
                if entrada[caractere].isalpha() or entrada[caractere].isnumeric() or entrada[caractere].isspace():
                    controle = 1
                    continue
                else:
                    print("\nEntrada inválida. Forneça uma nova entrada.")
                    controle = 0
                    break

        else:
            return entrada
        
        if controle:
            return entrada
        else:
            continue


class Artista(interfaceArtista):
    def __init__(self, nome : str, generoMusical : str) -> None:
        self.__nome = nome
        self.__generoMusical = generoMusical
        self.__listaDeMusicas = []

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def generoMusical(self) -> str:
        return self.__generoMusical
    
    @property
    def listaDeMusicas(self) -> list:
        return self.__listaDeMusicas
    
    @generoMusical.setter
    def generoMusical(self, generoMusical : str) -> None:
        self.__generoMusical = generoMusical

    def setGeneroMusical(self) -> None:
        self.__generoMusical = verificaEntrada()
    
    def addMusica(self, nome, album, duração, ano) -> None:

        keys = ("nome", "album", "duração", "ano")
        self.__listaDeMusicas.append(dict.fromkeys(keys))

        index = len(self.__listaDeMusicas) - 1

        ultimoItemDaLista = self.__listaDeMusicas[index]

        ultimoItemDaLista["nome"] = nome
        ultimoItemDaLista["album"] = album
        ultimoItemDaLista["duração"] = duração
        ultimoItemDaLista["ano"] = ano

