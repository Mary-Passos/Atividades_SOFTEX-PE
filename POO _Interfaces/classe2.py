class Ligavel:
    def ligar(self):
        pass

class Desligavel:
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Computador ligando...")
    
    def desligar(self):
        print("Computador desligando...")

computador = Computador()
computador.ligar()
computador.desligar()