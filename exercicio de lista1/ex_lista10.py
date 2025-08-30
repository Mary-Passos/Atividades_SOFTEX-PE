

import numpy as np


tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]

tabuleiro[0] = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']

tabuleiro[1] = ['pea' for _ in range(8)]


tabuleiro[7] = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']

tabuleiro[6] = ['pea' for _ in range(8)]


print("TABULEIRO DE XADREZ - POSIÇÃO INICIAL")
print("=" * 40)


tabuleiro_array = np.array(tabuleiro)
for i, linha in enumerate(tabuleiro_array):
    print(f"{8-i} | {' '.join(linha)}")
    
print("    " + " ".join([f" {chr(97+i)} " for i in range(8)]))