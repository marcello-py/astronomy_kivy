from book import *

l1 = Livro('edgar allan poe', 'Edgar Allan Poe', 1845)
l2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
m1= Membro('Marcelo', 3, [])
m2 = Membro('Rosa', 2, [])

b = Biblioteca([], [])
b.adicionar_membro(m1)
b.adicionar_membro(m2)
b.exibir_todos_membros()
b.adicionar_livro(l2)
b.exibir_todos_livros()