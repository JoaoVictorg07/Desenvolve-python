import random

num_elementos = (random.randint(5, 20))

elementos = [random.randint(1, 10) for _ in range(num_elementos)]
soma = sum(elementos)
media = soma / num_elementos

print(elementos)
print(f"A soma dos valores da lista é: {soma}")
print(f"A media dos valores da lista é: {media}")