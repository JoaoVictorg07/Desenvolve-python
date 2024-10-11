linha = "Alice de Sá, 29/12/1951"
linha.split('/')

mais_velha = ['', float('inf')]

for i in range(3):
    linha = input()
    primeiro_nome = linha.split()[0]
    ano_nascimento = int(linha.split('/')[-1])
    if ano_nascimento < mais_velha[1]:
        mais_velha[0] = primeiro_nome
        mais_velha[1] = ano_nascimento

print(mais_velha[0])