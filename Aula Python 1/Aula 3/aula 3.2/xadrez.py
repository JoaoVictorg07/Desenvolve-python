idade = int(input("Digite sua idade: "))
partidas = int(input("Quantas partidas você já jogou? ")) 
triunfos = int(input("Quantos jogos já venceu? "))

a = idade > 15 and idade < 19
b = partidas >= 3
c = triunfos >= 1

apto_a_jogar = a and b and c

print(apto_a_jogar)