'''10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.'''

notas = []


for aluno in range(2):
    print(f"\n=== ALUNO {aluno + 1} ===")
    
    
    notas_aluno = []
    

    for i in range(3):
        nota = float(input(f"Digite a {i+1}ª nota do aluno {aluno + 1}: "))
        notas_aluno.append(nota)
    

    notas.append(notas_aluno)

print(f"\nLista completa de notas: {notas}")


print("\n=== MÉDIAS ===")
for i, aluno_notas in enumerate(notas, 1):
    media = sum(aluno_notas) / len(aluno_notas)
    print(f"Aluno {i}: Média = {media:.2f}")

