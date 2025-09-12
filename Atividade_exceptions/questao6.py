'''Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.'''

class IdadeInvalidaError(Exception):

    def __init__(self, idade, mensagem="Idade inválida fornecida"):
        self.idade = idade
        self.mensagem = f"{mensagem}: {idade}"
        super().__init__(self.mensagem)

def cadastrar_idade(idade):

    if idade < 0:
        raise IdadeInvalidaError(idade, "Idade não pode ser negativa")
    return f"Idade {idade} cadastrada com sucesso!"

try:
    resultado = cadastrar_idade(25)
    print(resultado)
    
    resultado = cadastrar_idade(-5)  
    print(resultado)
    
except IdadeInvalidaError as e:
    print(f" Erro: {e}")