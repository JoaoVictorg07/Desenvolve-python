a = int(input("Digite a quantidade de elementos da lista 1: "))
b = int(input("Digite a quantidade de elementos da lista 2: "))

lista1, lista2 = []

for _ in range(a):
    lista1.append(int(input(f"Digite os {a} da a lista 1: ")))
    for _ in range(b):
        lista2.append(int(input("Digite os {b} da a lista 2: ")))


print(lista1)
print(lista1)