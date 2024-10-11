def resultado_votacao(votos):
    # Dicionário para armazenar o total de votos por candidato
    resultados = {}
    
    # Calcula o total de votos
    total_votos = 0
    for voto in votos:
        candidato = voto['candidato']
        quantidade_votos = voto['votos']
        
        # Atualiza o total de votos para cada candidato
        if candidato in resultados:
            resultados[candidato] += quantidade_votos
        else:
            resultados[candidato] = quantidade_votos
        
        total_votos += quantidade_votos

    # Calcula o percentual de votos para cada candidato
    for candidato in resultados:
        total = resultados[candidato]
        percentual = (total / total_votos) * 100 if total_votos > 0 else 0
        resultados[candidato] = (total, percentual)
    
    return resultados

# Exemplo de uso
votacao_exemplo = [
    {'candidato': 'Alice', 'votos': 150},
    {'candidato': 'Bob', 'votos': 200},
    {'candidato': 'Alice', 'votos': 100},
    {'candidato': 'Carlos', 'votos': 50},
    {'candidato': 'Bob', 'votos': 150},
]

resultado = resultado_votacao(votacao_exemplo)

# Imprimindo o resultado
print(resultado)
