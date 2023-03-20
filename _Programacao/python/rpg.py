from random import choice
from random import randint
import time

lista = ["Lobo"] 
''', "Ladrão", "Goblin"]'''
criatura = choice(lista)

hpPlayer = 100
caPlayer = 10

print()
print("Um", criatura, "aparece! ")

if criatura == "Lobo":
    hpLobo = 50
    print(hpLobo, "De HP")
    
    caLobo = 10
    iniciativaCriatura = randint(1,20) +1

    print()
    print('Role sua iniciativa!')
    iniciativaPlayer = input()
    iniciativaPlayer = randint(1,20) +20
    print()

    while hpLobo > 0:
        if iniciativaPlayer >= iniciativaCriatura:
            print(iniciativaPlayer, "Vs", iniciativaCriatura, "Seu Turno! ")
            print()
            print('Role seu teste de ataque!')

            testeDeAtaque = input()
            testeDeAtaque = randint(1,20)
            testeDeAtaqueBonus = testeDeAtaque +5

            print()

            if testeDeAtaque >= caLobo:
                print("Teste de ataque:", testeDeAtaque, "+ 5 =", testeDeAtaqueBonus)
                print("Classe de Armadura:", caLobo, "Você acertou o Lobo!")
                print("Role o Dano!")

                dano = input()
                dano = randint(1,8)
                danoBonus = dano +5
                print()

                hpLobo = hpLobo - danoBonus
                print(dano, "+ 5 =", danoBonus, "De dano")
                print(hpLobo, "De Hp")
                time.sleep(2)

                print("O lobo vai atacar! Contra-Atacar ou Esquivar?")
                ação = input()

                if ação == "Contra-Atacar":
                    print()
                    print("O Lobo vai atacar!")

                    testeDeAtaqueCriatura = randint(1,20) +1
                    print()
                    time.sleep(2)

                    if testeDeAtaqueCriatura >= caPlayer:
                        print("Teste de ataque:", testeDeAtaqueCriatura)
                        print("Sua Classe de Armadura:", caPlayer, "O Lobo te acertou!")
                        print("A criatura ira rolar o dano!")

                        time.sleep(2)
                        danoCriatura = randint(1,8) +1
                        print()

                        hpPlayer = hpPlayer - danoCriatura
                        print(danoCriatura, "De dano")
                        print(hpPlayer, "De Hp")
                        time.sleep(2)

                    elif testeDeAtaqueCriatura < caPlayer:
                        print("Teste de ataque:", testeDeAtaqueCriatura)
                        print("Sua Classe de Armadura:", caPlayer, "O Lobo errou!")
                        print("Role seu ataque para Contra-Atacar!")

                        testeDeAtaque2 = input()
                        testeDeAtaque2 = randint(1,20) +5

                        if testeDeAtaque2 >= caLobo:
                            print("Teste de ataque:", testeDeAtaque2)
                            print("Classe de Armadura", caLobo, "Você acertou o Lobo!")
                            print("Role o Dano!")

                            dano = randint(1,8) +5
                            print()

                            hpLobo = hpLobo - dano
                            print(dano, "De dano")
                            print(hpLobo, "De Hp")
                            time.sleep(2)

                        elif testeDeAtaque2 < caLobo:
                            print("Teste de Ataque:", testeDeAtaque2)
                            print("Classe de Armadura", caLobo, "Você errou o Lobo!")
                            print(hpLobo)

                elif ação == "Esquivar":
                    caPlayer = 15
                    print("O Lobo vai atacar!")

                    testeDeAtaqueCriatura = randint(1,20)
                    print()
                    time.sleep(2)

                    if testeDeAtaqueCriatura >= caPlayer:
                        print("Teste de ataque:", testeDeAtaqueCriatura)
                        print("Sua Classe de Armadura:", caPlayer, "O Lobo te acertou!")
                        print("A criatura ira rolar o dano!")

                        time.sleep(2)
                        danoCriatura = randint(1,8) +1
                        print()

                        hpPlayer = hpPlayer - danoCriatura
                        print(danoCriatura, "De dano")
                        print(hpPlayer, "De Hp")
                        time.sleep(2)

                    elif testeDeAtaqueCriatura < caPlayer:
                        print("Teste de ataque:", testeDeAtaqueCriatura)
                        print("Sua Classe de Armadura:", caPlayer, "O Lobo errou!")
                        print(hpLobo)
                        time.sleep(2)

            elif testeDeAtaque < caLobo:
                print("Teste de ataque:", testeDeAtaque)
                print("Sua Classe de Armadura:", caPlayer, "Você errou!")
                print(hpPlayer)
                time.sleep(2)

        elif iniciativaPlayer < iniciativaCriatura:
            print(iniciativaPlayer, "Vs", iniciativaCriatura, "A Criatura age primeiro!")
            print('A Criatura vai atacar! Contra-Atacar ou Esquivar?')
            input()        