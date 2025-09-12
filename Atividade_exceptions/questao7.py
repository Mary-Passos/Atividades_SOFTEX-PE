'''Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:

ValueError se o usuário digitar algo inválido

ZeroDivisionError se tentar dividir por zero'''

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print(f"Resultado: {num1} / {num2} = {resultado}")
    
except ValueError:
    print("Erro: Digite apenas números válidos!")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")