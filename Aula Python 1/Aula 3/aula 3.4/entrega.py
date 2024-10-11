distancia = int(input("Digite a distancia em km: "))
peso = float(input("Digite o peso do pacote em quilos: "))

if distancia <= 100:
    preco = peso * 1.00
elif distancia <= 300 and distancia > 100:
    preco = peso * 1.50
elif distancia > 300:
    preco = peso * 2

if peso >= 10:
    preco = preco + 10
    
print(f"O valor da entrega é R${preco:.2f}")
