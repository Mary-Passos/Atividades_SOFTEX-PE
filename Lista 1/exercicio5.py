'''5. Crie um programa em Python que simule uma competição entre candidatos,
avaliados por um grupo de avaliadores.'''


candidato1 = 0
candidato2 = 0
candidato3 = 0

print("Nota do avaliador 1 para o candidato 1:", end=" ")
candidato1 += float(input())
print("Nota do avaliador 1 para o candidato 2:", end=" ")
candidato2 += float(input())
print("Nota do avaliador 1 para o candidato 3:", end=" ")
candidato3 += float(input())

print("Nota do avaliador 2 para o candidato 1:", end=" ")
candidato1 += float(input())
print("Nota do avaliador 2 para o candidato 2:", end=" ")
candidato2 += float(input())
print("Nota do avaliador 2 para o candidato 3:", end=" ")
candidato3 += float(input())

print("Nota do avaliador 3 para o candidato 1:", end=" ")
candidato1 += float(input())
print("Nota do avaliador 3 para o candidato 2:", end=" ")
candidato2 += float(input())
print("Nota do avaliador 3 para o candidato 3:", end=" ")
candidato3 += float(input())

pontuacao1 = int(candidato1)
pontuacao2 = int(candidato2)
pontuacao3 = int(candidato3)

print("Pontuação final:")
print(f"Candidato 1: {pontuacao1}")
print(f"Candidato 2: {pontuacao2}")
print(f"Candidato 3: {pontuacao3}")

if pontuacao1 > pontuacao2 and pontuacao1 > pontuacao3:
    print("Candidato 1 é o campeão!")
elif pontuacao2 > pontuacao1 and pontuacao2 > pontuacao3:
    print("Candidato 2 é o campeão!")
elif pontuacao3 > pontuacao1 and pontuacao3 > pontuacao2:
    print("Candidato 3 é o campeão!")
else:
    print("Empate! Disputa acirrada")