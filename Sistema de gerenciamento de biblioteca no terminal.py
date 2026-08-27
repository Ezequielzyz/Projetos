class Livro:

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):

        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado com sucesso.")

        else:
            print(f"O livro {self.titulo} não está disponível para empréstimo.")

    def devolver(self):

        if not self.disponivel:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido com sucesso.")

        else:
            print(f"O livro {self.titulo} não está emprestado, portanto não pode ser devolvido.")

livro1 = Livro("Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

livro1.devolver()
livro1.emprestar()
livro1.emprestar()
livro1.devolver()