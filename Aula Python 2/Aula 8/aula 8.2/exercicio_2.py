def imprime_vogais_e_indices(frase):
    # Definindo as vogais
    vogais = "aeiouAEIOU"
    # Lista para armazenar as vogais e seus índices
    resultado = []

    # Usando enumerate para obter o índice e o caractere
    for indice, caracter in enumerate(frase):
        if caracter in vogais:  # Verificando se o caractere é uma vogal
            resultado.append((caracter, indice))  # Adiciona uma tupla com a vogal e seu índice

    # Imprimindo os resultados
    for vogal, indice in resultado:
        print(f"Vogal: {vogal}, Índice: {indice}")

# Exemplo de uso
frase = "Olá, como você está?"
imprime_vogais_e_indices(frase)
