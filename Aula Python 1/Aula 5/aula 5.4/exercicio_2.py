def soma_quadrados(a, b):
    return a**2 + b**2

if __name__ == "__main__":

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

resultado = soma_quadrados(n1, n2)
print(f"A soma dos quadrados de {n1} e {n2} é: {resultado}")

