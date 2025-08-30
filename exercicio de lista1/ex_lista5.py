'''5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".'''

livros = ["os miseraveis", "Anne", "Dom casmurro", "A culpas é das estrelas", "O médico e o monstro", "Duna"]
livros.remove("Silêncio dos inocentes")

if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
    print("Livro removido com sucesso!")
    print(livros)
else:
    print("Livro não encontrado")
