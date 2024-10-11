def soma_digitos(n):
    soma = 0
    while n > 0:
        soma += n % 10
        n //= 10
    return soma

if __name__ == "__main__":

    n = int(input("Digite um número: "))

resultado = soma_digitos(n)
print(f"A soma dos dígitos de {n} é: {resultado}")