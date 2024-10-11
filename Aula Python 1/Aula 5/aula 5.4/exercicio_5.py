import math

def calcula_perimetro_triangulo(a, b, c):
    return a + b + c

def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio

def calcula_perimetro_retangulo(a, b=None):
    if b is None:
        return 4 * a
    else:
        return 2 * (a + b)
    
def exibe_menu():
    print("\n--- Menu de Cálculo de Perímetro ---")
    print("1. Calcular o perímetro de um triângulo")
    print("2. Calcular o perímetro de um círculo")
    print("3. Calcular o perímetro de um retângulo (ou quadrado)")
    print("4. Sair")

# Programa principal
if __name__ == "__main__":
    while True:
        exibe_menu()  # Exibe o menu
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            # Calcula o perímetro do triângulo
            lado1 = int(input("Digite o valor do primeiro lado do triângulo: "))
            lado2 = int(input("Digite o valor do segundo lado do triângulo: "))
            lado3 = int(input("Digite o valor do terceiro lado do triângulo: "))
            perimetro_triangulo = calcula_perimetro_triangulo(lado1, lado2, lado3)
            print(f"O perímetro do triângulo é: {perimetro_triangulo}")

        elif opcao == 2:
            # Calcula o perímetro do círculo
            raio = int(input("Digite o valor do raio do círculo: "))
            perimetro_circulo = calcula_perimetro_circulo(raio)
            print(f"O perímetro do círculo é: {perimetro_circulo:.2f}")

        elif opcao == 3:
            # Calcula o perímetro do retângulo (ou quadrado)
            lado1 = int(input("Digite o valor do primeiro lado (ou lado do quadrado): "))
            lado2 = input("Digite o valor do segundo lado (ou deixe vazio se for quadrado): ")
            if lado2 == "":
                perimetro_retangulo = calcula_perimetro_retangulo(lado1)
            else:
                perimetro_retangulo = calcula_perimetro_retangulo(lado1, int(lado2))
            print(f"O perímetro do retângulo (ou quadrado) é: {perimetro_retangulo}")

        elif opcao == 4:
            # Sai do programa
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
