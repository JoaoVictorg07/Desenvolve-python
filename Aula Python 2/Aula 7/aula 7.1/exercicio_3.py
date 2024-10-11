frase = str(input("Digite a frase:"))

lst_espaço = 0
espaço = (" ")

for palavra in frase:
    if palavra == espaço:
        lst_espaço += 1

print(lst_espaço)