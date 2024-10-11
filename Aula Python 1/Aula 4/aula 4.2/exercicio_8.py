valor = 0

while True:
    valor = int(input('Digite um valor: '))
    if valor == ("Fim"):
        break
    
    elif valor == ("+"):
        valor += valor
    elif valor == ("-"):
        valor -= valor

    print(f"O valor é: {valor}")