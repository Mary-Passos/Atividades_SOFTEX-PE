'''Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.'''

try:
arquivo = open('dados.txt', 'r')
print("Arquivo aberto com sucesso")

finally:
print("Encerrando programa")
