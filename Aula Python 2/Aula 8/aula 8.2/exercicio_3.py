def ordenar_tuplas(alunos):
    # Ordena a lista de tuplas em ordem decrescente com base na média (segundo elemento da tupla)
    lista_ordenada = sorted(alunos, key=lambda x: x[1], reverse=True)
    return lista_ordenada

# Exemplo de uso
alunos = [("Alice", 7.5), ("Bob", 9.0), ("Carlos", 6.5), ("Diana", 8.0)]
lista_ordenada = ordenar_tuplas(alunos)

# Imprimindo a lista ordenada
print(lista_ordenada)
