from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        return "Carro andando"

try:
    carro = Carro()
except Exception as e:
    print(f"Erro ao instanciar Carro: {type(e).__name__}: {e}")

class CarroCorrigido(Transporte):
    def mover(self):
        return "Carro andando"
    
    def parar(self):
        return "Carro parado"

carro_corrigido = CarroCorrigido()
print(carro_corrigido.mover())  
print(carro_corrigido.parar())  