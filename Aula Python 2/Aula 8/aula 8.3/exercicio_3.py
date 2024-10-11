def mesclar_dicionarios(dict1, dict2):
    # Cria um novo dicionário para armazenar a fusão
    dicionario_fundido = dict1.copy()  # Começa com uma cópia do primeiro dicionário

    # Itera sobre o segundo dicionário
    for chave, valor in dict2.items():
        if chave in dicionario_fundido:
            # Se a chave já existe, pega o maior valor
            dicionario_fundido[chave] = max(dicionario_fundido[chave], valor)
        else:
            # Se a chave não existe, adiciona a nova chave e valor
            dicionario_fundido[chave] = valor

    return dicionario_fundido

# Exemplo de uso
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 3, 'c': 1, 'd': 4}

resultado = mesclar_dicionarios(dicionario1, dicionario2)

# Imprimindo o resultado
print(resultado)
