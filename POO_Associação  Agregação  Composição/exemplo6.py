class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = []
    
    def adicionar_comodo(self, nome_comodo):
        comodo = Comodo(nome_comodo)
        self.comodos.append(comodo)