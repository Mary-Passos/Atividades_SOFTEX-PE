from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Processando pagamento de R${valor:.2f} via Cartão de Crédito"

class Boleto(Pagamento):
    def processar(self, valor):
        return f"Processando pagamento de R${valor:.2f} via Boleto Bancário"

cartao = CartaoCredito()
boleto = Boleto()

print(cartao.processar(150.50))
print(boleto.processar(200.75))