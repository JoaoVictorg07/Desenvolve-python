def analisar_roteiro():
    # Nome do arquivo contendo o roteiro
    nome_arquivo = "estomago.txt"

    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
        
        # 1. Imprimir as primeiras 25 linhas
        print("Texto das primeiras 25 linhas:")
        for linha in linhas[:25]:
            print(linha.strip())
        
        # 2. Número de linhas do arquivo
        numero_linhas = len(linhas)
        print(f"\nNúmero total de linhas no arquivo: {numero_linhas}")
        
        # 3. Linha com o maior número de caracteres
        linha_mais_longa = max(linhas, key=len)
        print(f"\nLinha com maior número de caracteres:\n{linha_mais_longa.strip()}")
        print(f"Comprimento da linha: {len(linha_mais_longa)} caracteres")
        
        # 4. Número de menções aos nomes dos personagens "Nonato" e "Íria"
        conteudo = " ".join(linhas).lower()  # Transforma em minúsculas para contagem
        # Contagem exata para "nonato"
        mencoes_nonato = conteudo.count("nonato")
        # Contagem exata para "íria" usando delimitadores (ex. espaços, pontuações)
        mencoes_iria = sum(1 for word in conteudo.split() if word.strip(",.!?;:\"'").lower() == "íria")

        print(f"\nNúmero de menções ao personagem 'Nonato': {mencoes_nonato}")
        print(f"Número de menções ao personagem 'Íria': {mencoes_iria}")

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado. Verifique o caminho e o nome do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executa a função
analisar_roteiro()
