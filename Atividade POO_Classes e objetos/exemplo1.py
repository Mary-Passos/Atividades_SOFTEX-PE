class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Cleison gomes", 25)
pessoa2 = Pessoa("Maria Regina", 30)

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade} anos")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade} anos")