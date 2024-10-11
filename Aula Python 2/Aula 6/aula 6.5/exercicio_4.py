n = int(input("Digite o valor de n (dimensão da matriz): "))

matriz = [[i * j for j in range(n)] for i in range(n)]

for linha in matriz:
    print(linha)