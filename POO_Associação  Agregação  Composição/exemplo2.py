class Onibus:
    def __init__(self, numero, linha):
        self.numero = numero
        self.linha = linha

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def entrar_no_onibus(self, onibus):
        return f"{self.nome} entrou no ônibus {onibus.numero} da linha {onibus.linha}"