
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: Divisão por zero não é permitida!")
    return a / b

try:
    resultado = dividir(10, 2)
    print(f"10 / 2 = {resultado}")
    
    resultado = dividir(10, 0) =
    print(f"10 / 0 = {resultado}")

except ZeroDivisionError as e:
    print(e)