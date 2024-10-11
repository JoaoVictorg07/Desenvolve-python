def encontrar_elemento_faltando(lista1, lista2):
    # Converte as listas em sets
    set1 = set(lista1)
    set2 = set(lista2)
    
    # Verifica qual lista está desfalcada e encontra o elemento faltando
    if len(set1) > len(set2):
        elemento_faltando = set1 - set2  # Elemento em lista1 que não está em lista2
        lista_faltando = "segunda"
    else:
        elemento_faltando = set2 - set1  # Elemento em lista2 que não está em lista1
        lista_faltando = "primeira"
    
    # Retorna o resultado
    if elemento_faltando:
        return f"O elemento {elemento_faltando.pop()} está faltando na {lista_faltando} lista"
    else:
        return "Não há elementos faltando"

# Exemplo de uso
A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]

resultado = encontrar_elemento_faltando(A, B)
print(resultado)
