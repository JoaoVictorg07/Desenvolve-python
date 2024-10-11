n = int(input("Digite um número inteiro: "))
m = int(input("Digite outro número inteiro: "))

print(" ", end=" ")  # Espaço em branco antes dos números das colunas
for coluna in range(1, m + 1):
    print(coluna, end=" ")
print()  # Quebra de linha após o cabeçalho das colunas

for linha in range(1, n + 1):
    print(linha, end=" ")  # Cabeçalho da linha
    print("/ " * m)  # Imprime M caracteres "/" separados por espaço