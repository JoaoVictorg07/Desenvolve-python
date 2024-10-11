n = int(input("Digite um número: "))

maior = 0

while n > 0:
    x = int(input("Digite o valor de x: "))
    
    if x > maior:
        maior = x
    
    n = n - 1

# Imprime o maior valor encontrado
print("Maior:", maior)