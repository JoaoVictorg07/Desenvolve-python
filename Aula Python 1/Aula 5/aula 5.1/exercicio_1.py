n1 = float(input("Digite um número decimal: "))
n2 = float(input("Digite outro número decimal: "))

diferenca_absoluta = abs(n1 - n2)

diferenca_arredondada = round(diferenca_absoluta, 2)

print(f"A diferença absoluta entre {n1} e {n2} é: {diferenca_arredondada}")