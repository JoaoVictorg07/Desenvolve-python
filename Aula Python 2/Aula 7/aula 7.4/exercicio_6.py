import csv
from collections import defaultdict

def processar_musicas():
    # Nome do arquivo CSV
    nome_arquivo = 'spotify-2023.csv'
    
    # Dicionário para armazenar a música mais tocada de cada ano
    musicas_por_ano = defaultdict(lambda: ['', '', 0])  # (track_name, artist_name, streams)

    # Abre o arquivo para leitura
    with open(nome_arquivo, 'r', encoding='latin-1') as arquivo:
        leitor = csv.reader(arquivo)
        
        # Ignora o cabeçalho
        next(leitor)
        
        for linha in leitor:
            try:
                track_name = linha[0].strip('"')
                artist_name = linha[1].strip('"')
                artist_count = int(linha[2])
                released_year = int(linha[3])
                streams = int(linha[8])
                
                # Ignora músicas com mais de um artista e com caracteres especiais
                if artist_count > 1 or '"' in track_name or '"' in artist_name:
                    continue
                
                # Considera apenas os anos entre 2012 e 2022
                if 2012 <= released_year <= 2022:
                    # Se a música atual é mais tocada que a armazenada, atualiza
                    if streams > musicas_por_ano[released_year][2]:
                        musicas_por_ano[released_year] = [track_name, artist_name, streams]
                        
            except (IndexError, ValueError):
                # Ignora linhas com erros de indexação ou conversão
                continue

    # Cria uma lista com os resultados finais
    resultado = [[musica[0], musica[1], ano, musica[2]] 
                 for ano, musica in sorted(musicas_por_ano.items())]

    return resultado

# Executa a função e imprime o resultado
musicas = processar_musicas()
print(musicas)
