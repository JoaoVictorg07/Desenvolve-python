def fatorial(valor):
    # corpo da frnção
    fat = 1
    for i in range(1, valor+1):
        fat *= i
    return fat
    
n = int(input("Digite n: "))
meu_fatorial = fatorial(n)
print(f"{n}! é {meu_fatorial}")
 