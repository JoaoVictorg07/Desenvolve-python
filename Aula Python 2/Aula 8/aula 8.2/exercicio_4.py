def comprimir_tuplas(lista_tuplas):
    # Dicionário para armazenar a soma dos números para cada palavra
    dicionario = {}
    
    # Iterar sobre cada tupla na lista
    for palavra, numero in lista_tuplas:
        if palavra in dicionario:
            dicionario[palavra] += numero  # Soma o número se a palavra já estiver no dicionário
        else:
            dicionario[palavra] = numero  # Adiciona a palavra ao dicionário

    # Converte o dicionário de volta para uma lista de tuplas
    lista_comprimida = [(palavra, numero) for palavra, numero in dicionario.items()]
    
    return lista_comprimida

# Exemplo de uso
tuplas = [("maçã", 2), ("banana", 3), ("maçã", 4), ("laranja", 1), ("banana", 2)]
resultado = comprimir_tuplas(tuplas)

# Imprimindo o resultado
print(resultado)
