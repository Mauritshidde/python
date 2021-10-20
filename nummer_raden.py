import random

secret_number = random.randint(1,1000)
score = 50
door = True

while(door):
    keuze = int(input("kies een nummer tussen de 1 en 1000: "))
    if keuze == secret_number:
        print("je hebt het goed je score is" ,score)
        door = False
        break
    else:
        score -= 2
        if keuze > secret_number:
            print(keuze, "is groter dan het geheime getal")
        elif keuze < secret_number:
            print(keuze, "is kleiner dan het geheime getal")
