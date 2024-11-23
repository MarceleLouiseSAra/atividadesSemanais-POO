#Playlist.py

from interfaces import interfacePlaylist, interfaceManipularDados
import json

class Playlist(interfacePlaylist, interfaceManipularDados):
    def __init__(self, nome : str) -> None:
        self.__nome = nome
        self.__Playlist = []
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def Playlist(self) -> list:
        return self.__Playlist

    @nome.setter
    def nome(self, nome : str) -> None:
        self.__nome = nome

    def addMusica(self, musica : dict, nomeDoArtista : str) -> None:
        musica["artista"] = nomeDoArtista
        self.__Playlist.append(musica)

    def zerarPlaylist(self) -> None:
        self.__Playlist.clear()
        self.loadJSon()

    def excluirMusica(self, nomeDaMusica : str) -> None:
        for musica in self.__Playlist:
            if musica["nome"] == nomeDaMusica:
                self.__Playlist.remove(musica)

        self.writeJSon()

    def loadJSon(self):
        nomeDoArquivo = self.__nome + ".json"
        with open(nomeDoArquivo, "r") as arquivo:
            self.__Playlist = json.load(arquivo)
    
    def writeJSon(self):
        nomeDoArquivo = self.__nome + ".json"
        with open(nomeDoArquivo, "w") as arquivo:
            json.dump(self.__Playlist, arquivo, ensure_ascii = False, indent = 4)