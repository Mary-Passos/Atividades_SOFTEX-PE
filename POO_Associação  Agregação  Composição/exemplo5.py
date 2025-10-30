class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        print(f"Motor criado com {self.potencia} cavalos")
    
    def __del__(self):
        print(f"Motor de {self.potencia} cavalos destruído")


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)
        print(f"Carro {self.modelo} criado")
    
    def __del__(self):
        print(f"Carro {self.modelo} destruído")


carro = Carro("Fusca", 50)

del carro