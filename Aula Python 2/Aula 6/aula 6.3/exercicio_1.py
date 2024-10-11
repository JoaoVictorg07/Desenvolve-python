numeros = []

print("Digite números inteiros (digite 'done' para finalizar):")

while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == 'done':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro ou 'done' para finalizar.")

# Exibir a lista original
print(f"Lista original: {numeros}")

# Exibir os 3 primeiros elementos
print(f"Os 3 primeiros elementos: {numeros[:3]}")

# Exibir os 2 últimos elementos
print(f"Os 2 últimos elementos: {numeros[-2:]}")

# Exibir a lista invertida
print(f"Lista invertida: {numeros[::-1]}")

# Exibir os elementos de índice par
print(f"Elementos de índice par: {numeros[1::2]}")

# Exibir os elementos de índice ímpar
print(f"Elementos de índice ímpar: {numeros[::2]}")
