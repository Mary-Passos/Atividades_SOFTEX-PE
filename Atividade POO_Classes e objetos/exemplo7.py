class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class Turma:
    def __init__(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

aluno1 = Aluno("kevin", 8.5)
aluno2 = Aluno("cleison", 9.0)
aluno3 = Aluno("jurema fox", 7.5)

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

print("Alunos na turma:")
for aluno in turma.alunos:
    print(f"Nome: {aluno.nome}, Nota: {aluno.nota}")