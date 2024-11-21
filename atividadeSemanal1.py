#Crie uma classe "bolo";
class Bolo:
    def __init__(self, Nome, Recheio, Massa, Cobertura):
        self.Nome = Nome
        self.Recheio = Recheio
        self.Massa = Massa
        self.Cobertura = Cobertura

def cobertura(self):
    print(self.Nome, end= ': ')
    print(self.Cobertura)

#Crie umas instância da classe bolo;
bolo0 = Bolo("Toalha felpuda", "Beijinho", "Festa", True)

#Crie dois tipos (objetos) de bolo com os seguintes* atributos:
bolo1 = Bolo("Murango", "Morango", "Festa", True)
bolo2 = Bolo("Chuculate", "Brigadeiro", "Chocolate", False)

#Crie um terceiro bolo, igual ao primeiro, mas sem cobertura, advindo da instância principal:
bolo3a = Bolo("Murango", "Morango", "Festa", False)

#Printe na tela a cobertura de todos os bolos
bolo0.cobertura()
bolo1.cobertura()
bolo2.cobertura()
bolo3a.cobertura()

#Crie um terceiro bolo, igual ao primeiro, mas sem cobertura, advindo de bolo1 (um objeto já criado):
bolo3b = bolo1
bolo3b._Cobertura = False

#Printe na tela a cobertura de todos os bolos
print("\n")
bolo0.cobertura()
bolo1.cobertura()
bolo2.cobertura()
bolo3b.cobertura()
