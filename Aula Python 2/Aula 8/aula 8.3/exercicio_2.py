def contar_palavras(arquivo):
    # Dicionário para armazenar a contagem das palavras
    contagem = {}

    # Abre o arquivo e lê o conteúdo
    with open(arquivo, 'r', encoding='utf-8') as file:
        texto = file.read()
        
        # Remove pontuação e converte o texto para minúsculas
        texto = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in texto)
        
        # Divide o texto em palavras
        palavras = texto.split()
        
        # Contabiliza a ocorrência de cada palavra
        for palavra in palavras:
            if palavra in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1

    # Ordena o dicionário de forma decrescente pelas contagens
    contagem_ordenada = dict(sorted(contagem.items(), key=lambda item: item[1], reverse=True))
    
    return contagem_ordenada

# Caminho do arquivo
arquivo = 'estomago.txt'

# Chama a função e obtém a contagem de palavras
resultado = contar_palavras(arquivo)

# Imprimindo o dicionário ordenado
for palavra, quantidade in resultado.items():
    print(f"{palavra}: {quantidade}")
