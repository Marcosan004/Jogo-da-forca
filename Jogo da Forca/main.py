import random
palavra_secreta = ["futebol", "computador", "dinheiro", "celular"]
palavra_secreta = random.choice(palavra_secreta)
letras = []
ganhou = False
chances = 6
print("**Jogo da Forca**")
while True:
    for letra in palavra_secreta:
        if letra in letras:
            print(letra, end=' ')
        else:
            print("_", end=' ')
    print(f"Vôce tem {chances} chances!")
    tentativa = input("Escolha uma letra para adivinhar: ")
    letras.append(tentativa)
    if tentativa not in palavra_secreta:
        chances -= 1

    ganhou = True
    for letra in palavra_secreta:
        if letra not in letras:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns! vôce ganhou. A palavra era: {palavra_secreta}")
else:
    print(f"Vôce perdeu a palavra era: {palavra_secreta}")