produto = 1

while True:
    valor = int(input("Digite um valor: "))
    if valor == 0:
        break

    if valor > 0:
        produto *= valor

print(f"Produto: {produto}") 