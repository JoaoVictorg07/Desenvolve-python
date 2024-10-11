eh_par = lambda x: "par" if x % 2 == 0 else "ímpar"

# Programa principal
if __name__ == "__main__":
    while True:
        # Solicita ao usuário um número
        numero = int(input("Digite um número (ou 0 para sair): "))

        # Verifica se o usuário digitou 0 para sair
        if numero == 0:
            print("Saindo do programa...")
            break

        # Chama a função lambda para verificar se é par ou ímpar
        resultado = eh_par(numero)
        print(f"O número {numero} é {resultado}.")