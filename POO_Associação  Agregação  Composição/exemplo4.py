class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
    
    def __str__(self):
        return f"{self.nome} ({self.posicao})"
    
    def __repr__(self):
        return f"Jogador(nome='{self.nome}', posicao='{self.posicao}')"


class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
    
    def adicionar_jogador(self, jogador):
        if isinstance(jogador, Jogador):
            self.jogadores.append(jogador)
        else:
            raise TypeError("O objeto deve ser uma instância de Jogador")
    
    def remover_jogador(self, jogador):
        if jogador in self.jogadores:
            self.jogadores.remove(jogador)
    
    def listar_jogadores(self):
        if not self.jogadores:
            print(f"O time {self.nome} não tem jogadores.")
            return
        
        print(f"Jogadores do time {self.nome}:")
        for i, jogador in enumerate(self.jogadores, 1):
            print(f"{i}. {jogador}")
    
    def __str__(self):
        return f"Time: {self.nome} ({len(self.jogadores)} jogadores)"
    
    def __repr__(self):
        return f"Time(nome='{self.nome}', jogadores={self.jogadores})"