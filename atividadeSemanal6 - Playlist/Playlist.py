#Playlist.py

from interfaces import interfacePlaylist

class Playlist:
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

    def excluirMusica(self, nomeDaMusica : str) -> None:
        for musica in self.__Playlist:
            if musica["nome"] == nomeDaMusica:
                self.__Playlist.remove(musica)