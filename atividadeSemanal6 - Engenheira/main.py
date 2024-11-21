#main.py

from Formas import Quadrado, Retangulo
from Engenheira import Engenheira


terreno0 = Quadrado()
terreno1 = Retangulo()

Engenheira0 = Engenheira("Marcele")

Engenheira0.medirArea(terreno1)
Engenheira0.medirPerimetro(terreno1)
Engenheira0.medirArea(terreno0)
Engenheira0.medirPerimetro(terreno0)