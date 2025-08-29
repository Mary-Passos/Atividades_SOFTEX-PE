#3. Crie um programa em Python que simule a venda de ingressos para um show. 

print("=== Venda de Ingressos ===")

pessoas = int(input("Quantas pessoas vão ao show? "))

total_pagar = 0

for i in range(1, pessoas + 1):
    idade = int(input(f"Idade da pessoa {i}: "))
    
    if idade <= 12:
        print("Entrada grátis")
    elif 13 <= idade <= 17:
        print("Meia entrada (R$ 10)")
        total_pagar += 10
    else:
        print("Ingresso inteiro (R$ 20)")
        total_pagar += 20

print(f"Total a pagar: R$ {total_pagar}")