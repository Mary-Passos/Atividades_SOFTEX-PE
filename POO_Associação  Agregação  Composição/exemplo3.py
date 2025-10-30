class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)