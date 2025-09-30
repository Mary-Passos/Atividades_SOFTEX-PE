class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_informacoes(self):
        return f"{self.marca} {self.modelo} - Ano {self.ano}"

o_carro = Carro("Bugatti", "La Voiture Noire", 2019)

print("ANTES da alteração:")
print(o_carro.exibir_informacoes())
print()

o_carro.ano = 2022

print("DEPOIS da alteração:")
print(o_carro.exibir_informacoes())