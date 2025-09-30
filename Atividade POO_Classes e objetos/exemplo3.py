class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Bugatti", "La Voiture Noire", 2019)
carro2 = Carro("Rolls-Royce", "Sweptail", 2017)
carro3 = Carro("Ferrari", " 250 GTO", 1962)

print(f"Carro 1: {carro1.marca} {carro1.modelo} - Ano {carro1.ano}")
print(f"Carro 2: {carro2.marca} {carro2.modelo} - Ano {carro2.ano}")
print(f"Carro 3: {carro3.marca} {carro3.modelo} - Ano {carro3.ano}")
