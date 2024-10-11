from collections import Counter

def diferenca_listas(lista1, lista2):
    # Contagem dos elementos nas duas listas
    contagem1 = Counter(lista1)
    contagem2 = Counter(lista2)

    # Encontrar a diferença entre os contadores
    diferenca = contagem1 - contagem2

    # Expandir o resultado para uma lista incluindo elementos duplicados
    resultado = list(diferenca.elements())

    return resultado

lista1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lista2 = [1, 1, 2, 4, 5, 6]

resultado = diferenca_listas(lista1, lista2)
print(resultado)