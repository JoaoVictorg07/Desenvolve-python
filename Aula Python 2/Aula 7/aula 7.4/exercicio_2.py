import re

def processar_frase():
    # Nome dos arquivos
    nome_arquivo_origem = "frase.txt"
    nome_arquivo_destino = "palavras.txt"
    
    # Lê o conteúdo do arquivo "frase.txt"
    with open(nome_arquivo_origem, 'r') as arquivo_origem:
        conteudo = arquivo_origem.read()
    
    # Remove caracteres não alfabéticos e separa as palavras
    palavras = re.findall(r'\b[A-Za-z]+\b', conteudo)
    
    # Salva cada palavra em uma linha no arquivo "palavras.txt"
    with open(nome_arquivo_destino, 'w') as arquivo_destino:
        for palavra in palavras:
            arquivo_destino.write(palavra + '\n')
    
    # Lê e imprime o conteúdo do arquivo "palavras.txt"
    with open(nome_arquivo_destino, 'r') as arquivo_destino:
        conteudo_palavras = arquivo_destino.read()
        print("Conteúdo do arquivo 'palavras.txt':")
        print(conteudo_palavras)

# Executa a função
processar_frase()
