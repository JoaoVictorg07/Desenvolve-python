soma = 0

for i in range(10):
    while True:
        valor = int(input(f"Digite o valor inteiro positivo {i + 1}: "))
        if valor > 0:
            break
        else:
            print("Valor inválido, digite um número inteiro positivo.")

    soma += valor

media = soma / 10

print(f"A média dos valores digitados é: {media:.2f}")