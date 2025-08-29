#1. Crie um programa em Python que simule um torneio de futebol da seleção

vitorias = 0
empates = 0
derrotas = 0

for i in range(1, 6):
    print(f"Gols da Seleção no jogo {i}:", end=" ")
    gols_selecao = int(input())
    print(f"Gols do adversário no jogo {i}:", end=" ")
    gols_adversario = int(input())
    
    if gols_selecao > gols_adversario:
        vitorias += 1
    elif gols_selecao == gols_adversario:
        empates += 1
    else:
        derrotas += 1

print("=== Torneio de Futebol ===")
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")