from random import choice
from random import randint
import time

class Entidade:
    def __init__(self, tipo, hp, ca, bonusIniciativa):
        self.tipo = tipo
        self.hp = hp
        self.ca = ca
        self.iniciativa = randint(1, 20) + bonusIniciativa

    def acertoDeAtaque(self):
        acerto = randint(1,20)
        return acerto
    
    def danoDeAtaque(self, max):
        dano = randint(1, max)
        return dano

player = Entidade(tipo="P",hp=100, ca=15, bonusIniciativa=5)
lobo = Entidade(tipo="C", hp=50, ca=10, bonusIniciativa=1)

ordem = []
vez = 0

print("Iniciativa do Player ", player.iniciativa)
print("Iniciativa da Criatura ", lobo.iniciativa)

if player.iniciativa >= lobo.iniciativa:
    ordem.append(player)
    ordem.append(lobo)
    input("Iniciativa do Player, Pressione Enter para rolar o dado > ")
else:
    ordem.append(lobo)
    ordem.append(player)
    input("Iniciativa da Criatura, A Criatura Rolou seu ataque!")

while player.hp > 0 and lobo.hp > 0:

    print("\nVez de ", ordem[vez].tipo)    

    acertoDeAtaque = ordem[vez].acertoDeAtaque()
    print("Acerto de Ataque: ", acertoDeAtaque)

    if ordem[vez].tipo=="P":
        danoDeAtaque = ordem[vez].danoDeAtaque(10)
    elif ordem[vez].tipo=="C":
        danoDeAtaque = ordem[vez].danoDeAtaque(8)

    if vez == 0:
        if acertoDeAtaque >= ordem[1].ca:
            print("Dano de Ataque: ", danoDeAtaque)
            ordem[1].hp -= danoDeAtaque
            print("Hp do " + str(ordem[1].tipo) + ": " + str(ordem[1].hp))
        else:
            print("Errou o Ataque!")

    elif vez == 1:
        if acertoDeAtaque >= ordem[0].ca:
            print("Dano de Ataque: ", danoDeAtaque)
            ordem[0].hp -= danoDeAtaque
            print("Hp do " + str(ordem[0].tipo) + ": " + str(ordem[0].hp))
        else:
            print("Errou o Ataque!")

    input("Pressione Enter para a próxima rodada > ")

    vez += 1
    if vez > 1:
        vez = 0

if player.hp > lobo.hp:
    print("Player Matou o Lobo! Venceu!")
else:
    print("Se Fdueu! Lobo te ESTRAÇALHOu!")