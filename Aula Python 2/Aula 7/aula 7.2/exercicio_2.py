# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Lista de vogais para substituição
vogais = "aeiouAEIOU"

# Substitui cada vogal por '*'
frase_sem_vogal = ''.join(['*' if letra in vogais else letra for letra in frase])

# Exibe a frase modificada
print(f"Frase modificada: {frase_sem_vogal}")
