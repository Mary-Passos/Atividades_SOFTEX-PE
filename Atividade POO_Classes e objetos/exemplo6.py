class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado. Saldo atual: R$ {self.saldo}")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado. Saldo atual: R$ {self.saldo}")
            return True
        else:
            print(f"Saldo insuficiente. Saldo atual: R$ {self.saldo}")
            return False

conta = ContaBancaria("Carlos", 500)

print("=== Teste 1: Saque com saldo suficiente ===")
resultado = conta.sacar(200)
if resultado:
    print("Saque autorizado!")
else:
    print("Saque negado!")

print("\n=== Teste 2: Saque com saldo insuficiente ===")
resultado = conta.sacar(400)
if resultado:
    print("Saque autorizado!")
else:
    print("Saque negado!")

print("\n=== Teste 3: Saque bem-sucedido ===")
resultado = conta.sacar(100)
if resultado:
    print("Saque autorizado!")
else:
    print("Saque negado!")