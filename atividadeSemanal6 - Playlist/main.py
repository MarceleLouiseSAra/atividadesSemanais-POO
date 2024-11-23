#main.py

from Playlist import Playlist
from Artista import Artista

tay = Artista("Taylor Swift", "pop")

tay.writeJSon() #escreve json vazio

tay.addMusica("coney island", "evermore", "4min35s", "2021")
tay.addMusica("'tis the damn season'", "evermore", "3min49s", "2021")
tay.addMusica("no body, no crime", "evermore", "3min35s", "2021")

tay.writeJSon()

brina = Artista("Sabrina Carpenter", "pop")

brina.addMusica("bed chem", "Short 'n Sweet", "2min51s", "2024")
brina.addMusica("Please Please Please", "Short 'n Sweet", "3min06s", "2024")
brina.addMusica("Espresso", "Short 'n Sweet", "2min54s", "2024")

brina.writeJSon()

for_evermore = Playlist("for evermore")

for_evermore.addMusica(tay.listaDeMusicas[1], tay.nome)
for_evermore.addMusica(brina.listaDeMusicas[1], brina.nome)

print(f"\n{for_evermore.nome}, {for_evermore.Playlist}")

for_evermore.writeJSon()