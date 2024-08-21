#Leitura de dados (entrada)
comprimento = int(input("Digite o comprimento: "))
largura = int(input("Digite a largura: "))
preço_m2 = int(input("Valor do m2: "))

#processamento
area = comprimento * largura #m2
preço_total = area * preço_m2

#Impressão de dados (saída)
print(f"O terreno possui {area}m2 e custa R${preço_total:,.2f}")