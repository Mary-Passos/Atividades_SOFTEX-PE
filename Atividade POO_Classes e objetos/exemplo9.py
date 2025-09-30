class Cachorro:
    especie = "Canis familiaris"
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

cachorro1 = Cachorro("Rapadura", 3)
cachorro2 = Cachorro("florentina", 5)

print("Acessando pela classe:")
print(f"Cachorro.especie: {Cachorro.especie}")

print("\nAcessando pelos objetos:")
print(f"cachorro1.especie: {cachorro1.especie}")
print(f"cachorro2.especie: {cachorro2.especie}")

print("\nAtributos de instância:")
print(f"cachorro1.nome: {cachorro1.nome}, cachorro1.idade: {cachorro1.idade}")
print(f"cachorro2.nome: {cachorro2.nome}, cachorro2.idade: {cachorro2.idade}")