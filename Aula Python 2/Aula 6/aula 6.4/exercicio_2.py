frase = input("Digite uma frase: ").lower()

# Definir as vogais
vogais = "aeiouAEIOU"

# Usando compreensão de lista para obter as vogais, ordenadas alfabeticamente
lista_vogais = sorted([letra for letra in frase if letra in vogais])

# Usando compreensão de lista para obter as consoantes (removendo os espaços em branco)
lista_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]

print(f"Lista de vogais (ordenada): {lista_vogais}")
print(f"Lista de consoantes (sem espaços): {lista_consoantes}")