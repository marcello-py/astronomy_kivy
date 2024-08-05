class Livro:
    def __init__(self, titulo: str, autor: str, ano: int) -> None:
    # Métodos: exibir informações do livro, marcar como emprestado, marcar como devolvido.
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
    
    def exibir_informacoes(self) -> str:
        return f'informações: Livro {self.titulo}, Autor {self.autor}, Ano {self.ano}, Disponível {self.disponivel}'

    def marcar_como_emprestado(self) -> None:
        self.disponivel = False
        
    
    def marcar_como_devolvido(self) -> None:
        self.disponivel = True                                                
        

class Membro:
    def __init__(self, nome: str, id_membro: str, livros_emprestados: list = None) -> None:
    # Métodos: exibir informações do membro, pegar emprestado um livro, devolver um livro.
        self.nome = nome
        self.id_membro = id_membro
        self.livros_emprestados = livros_emprestados if livros_emprestados is not None else []

    def exibir_informacoes(self) -> str:
        return f'Informações de Membro: {self.nome}, ID:{self.id_membro}'
    
    def pegar_emprestado(self, livro: Livro) -> None:
        self.livros_emprestados.append(livro)       

    def devolver_livro(self, livro:Livro) -> None:
        self.livros_emprestados.remove(livro)
       

class Biblioteca:
# Métodos: adicionar livro, remover livro, adicionar membro, remover membro, emprestar livro, 
# devolver livro, exibir todos os livros, exibir todos os membros.
    def __init__(self, lista_livros: list = None, lista_membros: list = None) -> None:
        self.lista_livros = lista_livros if lista_livros is not None else []
        self.lista_membros = lista_membros if lista_membros is not None else []

    def adicionar_livro(self, livro: Livro) -> None:
        self.lista_livros.append(livro)
    
    def remover_livro(self, livro: Livro) -> None:
        self.lista_livros.remove(livro)

    def adicionar_membro(self, membro: Membro) -> None:
        self.lista_membros.append(membro)
    
    def remover_membro(self, membro: Membro) -> None:
        self.lista_membros.remove(membro)
    
    def emprestar_livro(self, livro: Livro, membro: Membro) -> None:
        if livro in self.lista_livros and livro.disponivel:
            livro.marcar_como_emprestado()
            membro.pegar_emprestado(livro)

    def devolver_livro(self, livro: Livro, membro: Membro) -> None:
        if livro in membro.livros_emprestados:
            livro.marcar_como_devolvido()
            membro.devolver_livro(livro)
    
    def exibir_todos_livros(self) -> None:
        for livro in self.lista_livros:
            print(livro.exibir_informacoes())

    def exibir_todos_membros(self) ->None:
        for membro in self.lista_membros:
            print(membro.exibir_informacoes())

