def filtrar_dicionario(dicionario, chaves):
    # Cria um novo dicionário filtrado
    dicionario_filtrado = {chave: dicionario[chave] for chave in chaves if chave in dicionario}
    return dicionario_filtrado

# Exemplo de uso
dicionario_exemplo = {
    'nome': 'Alice',
    'idade': 25,
    'cidade': 'São Paulo',
    'profissao': 'Engenheira'
}

lista_chaves = ['nome', 'cidade', 'pais']  # 'pais' não está no dicionário

resultado = filtrar_dicionario(dicionario_exemplo, lista_chaves)

# Imprimindo o resultado
print(resultado)
