# 2 Crie um programa em Python que simule um jogo de adivinhação. 

import random

numero_secreto = random.randint(1, 20)
tentativas = 5
acertou = False

while tentativas > 0 and not acertou:
    palpite = int(input("Adivinhe o número (1-20): "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        acertou = True
    else:
        tentativas -= 1
        if palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")
        print(f"Tentativas restantes: {tentativas}")

if not acertou:
    print(f"Game over! O número era {numero_secreto}")