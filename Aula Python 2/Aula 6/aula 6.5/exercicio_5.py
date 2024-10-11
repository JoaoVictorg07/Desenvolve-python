def pares_unicos(numeros, soma_objetivo):
    pares = set()  # Usamos um conjunto para evitar pares duplicados
    vistos = set()  # Conjunto para armazenar os números já vistos

    for num in numeros:
        complemento = soma_objetivo - num  # Encontrar o complemento para formar a soma

        if complemento in vistos:  # Se o complemento já foi visto, temos um par
            # Adicionamos o par ordenado para garantir que (3,7) e (7,3) sejam iguais
            pares.add(tuple(sorted((num, complemento))))
        
        vistos.add(num)  # Adicionar o número atual aos números já vistos
    
    return list(pares)  # Retornar o conjunto convertido para lista

nums = [3, 4, 5, 6, 7]
soma = 10
resultado = pares_unicos(nums, soma)
print(resultado)  # Saída esperada: [(3, 7), (4, 6)]