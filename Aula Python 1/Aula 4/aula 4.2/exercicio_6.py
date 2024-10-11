maior = 0
menor = 0

while True:
    valor = int(input("Digite um número: "))
    if maior is 0 or valor > maior:
        maior = valor
    if menor is 0 or valor < menor:
        menor = valor
    elif valor == 0:
        break

print(f"Maior valor digitado: {maior}")
print(f"Menor valor digitado: {menor}")