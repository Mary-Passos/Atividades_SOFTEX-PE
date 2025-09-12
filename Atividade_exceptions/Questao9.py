'''Crie uma função sacar(saldo, valor) que:

Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.

Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.'''

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        super().__init__(f"Saldo insuficiente! Saldo: R${saldo:.2f}, Tentativa de saque: R${valor:.2f}")

def sacar(saldo, valor):

    if valor <= 0:
        raise ValueError("Valor do saque deve ser positivo!")
    
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    
    return saldo - valor

try:
    saldo_atual = 1000.00
    valor_saque = 500.00
    
    novo_saldo = sacar(saldo_atual, valor_saque)
    print(f" Saque de R${valor_saque:.2f} realizado com sucesso!")
    print(f" Novo saldo: R${novo_saldo:.2f}")
    
except SaldoInsuficienteError as e:
    print(f" {e}")
except ValueError as e:
    print(f" {e}")