'''Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:

try para a conversão,

else para verificar se é par ou ímpar,
finally para exibir "Fim do programa".'''
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Digite apenas números inteiros!")
else:
    if numero % 2 == 0:
        print(f"O número {numero} é PAR")
    else:
        print(f"O número {numero} é ÍMPAR")
finally:
    print("Fim do programa")