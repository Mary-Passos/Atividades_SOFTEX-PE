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
        else:
            print(f"Saldo insuficiente. Saldo atual: R$ {self.saldo}")

conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria")

print("=== Conta 1 ===")
conta1.depositar(500)
conta1.sacar(300)
conta1.sacar(1500)

print("\n=== Conta 2 ===")
conta2.depositar(200)
conta2.sacar(100)
conta2.sacar(150)