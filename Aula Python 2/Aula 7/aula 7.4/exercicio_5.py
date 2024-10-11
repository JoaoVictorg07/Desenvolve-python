def criar_csv_livros():
    # Lista de livros com título, autor, ano de publicação e número de páginas
    livros = [
        ["1984", "George Orwell", 1949, 328],
        ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
        ["Dom Casmurro", "Machado de Assis", 1899, 288],
        ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
        ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
        ["A Revolução dos Bichos", "George Orwell", 1945, 112],
        ["Orgulho e Preconceito", "Jane Austen", 1813, 432],
        ["O Alquimista", "Paulo Coelho", 1988, 208],
        ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
        ["A Menina que Roubava Livros", "Markus Zusak", 2005, 552]
    ]
    
    # Nome do arquivo CSV
    nome_arquivo = "meus_livros.csv"
    
    # Abre o arquivo para escrita
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        # Escreve o cabeçalho
        arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
        
        # Escreve as informações de cada livro
        for livro in livros:
            linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
            arquivo.write(linha)

# Executa a função para criar o arquivo CSV
criar_csv_livros()
