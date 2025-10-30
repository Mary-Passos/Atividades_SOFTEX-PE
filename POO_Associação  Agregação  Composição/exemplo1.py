class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.livros = []  
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def listar_livros(self):
        return self.livros

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

if __name__ == "__main__":

    pessoa1 = Pessoa("Jessica", 25)
    pessoa2 = Pessoa("Bruno", 30)
    
    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("1984", "George Orwell")
    livro3 = Livro("O Cortiço", "Aluísio Azevedo")
    
    pessoa1.adicionar_livro(livro1)
    pessoa1.adicionar_livro(livro2)
    pessoa2.adicionar_livro(livro3)
    
    print(f"{pessoa1.nome} possui os livros:")
    for livro in pessoa1.listar_livros():
        print(f"- {livro.titulo} de {livro.autor}")
    
    print(f"\n{pessoa2.nome} possui os livros:")
    for livro in pessoa2.listar_livros():
        print(f"- {livro.titulo} de {livro.autor}")