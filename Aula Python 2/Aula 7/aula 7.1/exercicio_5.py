frase = "O meu amor mora em Roma e me deu um ramo de flores."

cont_vogais = 0
indice = []

for i in range(len(frase)):
    if frase[i] in 'aeiouAEIOU':
        cont_vogais += 1
        indice.append(i)

print(cont_vogais)
print(indice)