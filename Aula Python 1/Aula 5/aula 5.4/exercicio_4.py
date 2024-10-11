def inverteValor(valor):
    # corpo da função
    valor_invertido = 0
    while valor > 0:
        # Obtém o último dígito e adiciona ao invertido
        valor_invertido = valor_invertido * 10 + valor % 10
        # Remove o último dígito do número original
        valor = valor // 10
    return valor_invertido

def verificaInverso(valor, valor_invertido):
    #############
    # corpo da função
    return (valor % 2 == valor_invertido % 2)

if __name__ == "__main__":
    # Solicita um valor do usuário
    valor = int(input("Digite um valor inteiro: "))

    # Chama a função inverteValor
    valor_invertido = inverteValor(valor)

    # Exibe o valor invertido
    print(f"Valor invertido: {valor_invertido}")

    # Chama a função verificaInverso
    resultado = verificaInverso(valor, valor_invertido)

    # Exibe se o valor original e o invertido são ambos par ou ambos ímpar
    if resultado:
        print("O valor original e o valor invertido são ambos par ou ambos ímpar.")
    else:
        print("O valor original e o valor invertido são diferentes em relação à paridade.")