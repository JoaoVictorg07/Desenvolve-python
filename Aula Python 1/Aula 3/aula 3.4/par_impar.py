n1 = int(input("Digite um número: "))
n2 = int(input("Digite um outro número: "))

soma = n1 + n2

def verificação(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
resultado = verificação(soma)

print(f"A soma dos números é {soma}, que é {resultado}.")
