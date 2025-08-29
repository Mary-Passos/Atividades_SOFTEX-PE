'''6. Crie um programa em Python que ajude um professor a verificar a situação de um
aluno.'''

nome = input("Digite o nome do aluno: ")

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    situacao = "APROVADO"
elif nota >= 5:
    situacao = "REPOSIÇÃO"
else:
    situacao = "REPROVADO"

print(f"{nome} está em {situacao}!")