'''Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.'''

try:
    numero = int(input("digite umnúmero inteiro:"))
except ValueError:
    print("Apenas números inteiros!")
else:
    print(f"Converaõ bem sucedida! Você digitou: {numero}")
