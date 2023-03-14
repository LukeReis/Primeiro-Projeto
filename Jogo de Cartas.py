import random

nome_jogador1 = str(input("Informe o nome do Jogador 1: "))
nome_jogador2 = str(input("Informe o nome do Jogador 2: "))

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self):
        valores = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]
        naipes = ["Copas", "Espadas", "Ouros", "Paus"]
        self.cartas = [Carta(valor, naipe) for valor in valores for naipe in naipes]

    def Embaralhar(self):
        random.shuffle(self.cartas)

    def darCarta(self):
        return self.cartas.pop()

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []

    def addCartas(self, carta):
        self.cartas.append(carta)

    def mostrarCartas(self):
        return f"{self.nome} tem as seguintes cartas:\n" + "\n".join([str(carta) for carta in self.cartas])

baralho = Baralho()
baralho.Embaralhar()

jogador1 = Jogador(nome_jogador1)
jogador2 = Jogador(nome_jogador2)

for i in range(2):
    jogador1.addCartas(baralho.darCarta())
    jogador2.addCartas(baralho.darCarta())

print(jogador1.mostrarCartas())
print(jogador2.mostrarCartas())