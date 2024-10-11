import random

valor = random.randint(1, 10)

while True:

    n = int(input("Adivinhe o número entre 1 e 10: "))

    if n > valor:
        print("Tente um número menor!")
    elif n < valor:
        print("Tente um número maior!")
    else:
        print(f"Correto! O número é {valor}.")
        break
