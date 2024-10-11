def tem_elementos_comuns(lista1, lista2):
    # Converte as listas em sets
    set1 = set(lista1)
    set2 = set(lista2)
    
    # Verifica se a interseção dos dois sets é não vazia
    return not set1.isdisjoint(set2)

# Exemplo de uso
lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
lista_c = [10, 11, 12]

print(tem_elementos_comuns(lista_a, lista_b))  # Saída: True
print(tem_elementos_comuns(lista_a, lista_c))  # Saída: False
