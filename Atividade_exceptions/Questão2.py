'''Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.'''

try:

    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
     
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação do {numero1} * {numero2} é: {resultado}")
 
except ValueError:

    print("Erro: Digite apenas números válidos!")