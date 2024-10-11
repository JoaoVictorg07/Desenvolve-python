# Leia o número de experimentos
n = int(input("Digite a quantidade de experimentos: "))

total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Loop para ler a quantidade e o tipo de cada cobaia utilizada
for _ in range(n):
    entrada = input("Digite a quantidade de cobaias e o tipo (S, R, C): ").split()
    quantia = int(entrada[0])
    tipo = entrada[1].upper()

    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

# Soma do total de cobaias utilizadas
total_cobaias = total_sapos + total_ratos + total_coelhos

# Soma do percentual de cada tipo de cobaia em relação ao total
percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
