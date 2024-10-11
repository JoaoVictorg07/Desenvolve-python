def atividades_comuns(turmas):
    # Verifica se a lista de turmas não está vazia
    if not turmas:
        return set()  # Retorna um conjunto vazio se não houver turmas
    
    # Inicializa o conjunto de atividades comuns com a primeira turma
    atividades_comuns = set(turmas[0])
    
    # Realiza a interseção com os conjuntos de atividades das demais turmas
    for turma in turmas[1:]:
        atividades_comuns.intersection_update(set(turma))
    
    return atividades_comuns

# Exemplo de uso
turmas = [
    ["futebol", "vôlei", "música"],
    ["vôlei", "música", "teatro"],
    ["música", "teatro", "ações comunitárias"],
    ["música", "futebol", "ações comunitárias"]
]

atividades = atividades_comuns(turmas)
print("Atividades comuns a todas as turmas:", atividades)
