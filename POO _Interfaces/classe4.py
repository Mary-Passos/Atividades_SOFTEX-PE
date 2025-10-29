class Repositorio:
    def salvar(self, objeto):
        pass
    
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Salvando objeto: {objeto}")

try:
    repositorio = RepositorioMemoria()
    print("Instância criada com sucesso")
except TypeError as e:
    print(f"Erro: {e}")

#corrigindo CÒD

class Repositorio:
    def salvar(self, objeto):
        pass
    
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Salvando objeto: {objeto}")
    
    def buscar(self, id):
        print(f"Buscando objeto com id: {id}")
        return f"Objeto_{id}"

repositorio = RepositorioMemoria()
repositorio.salvar("Dados importantes")
resultado = repositorio.buscar(1)
print(f"Resultado da busca: {resultado}")