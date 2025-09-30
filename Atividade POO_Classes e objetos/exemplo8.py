class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

aluno1 = Aluno("João", 8.5)
aluno2 = Aluno("Maria", 9.0)
aluno3 = Aluno("Pedro", 7.5)

print(aluno1)
print(aluno2)
print(aluno3)

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

print("\nAlunos na turma:")
for aluno in turma.alunos:
    print(aluno)