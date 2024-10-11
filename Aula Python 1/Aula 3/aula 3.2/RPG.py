classe = str(input("Escolha uma classe: "))
força = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))

a = classe = "guerreiro" and força >= 15 and magia < 10
b = classe = "mago" and força < 10 and magia >= 15
c = classe = "arqueiro" and força > 5 and força < 15 and magia > 5 and magia < 15

pontos_certos = a or b or c

print(pontos_certos)