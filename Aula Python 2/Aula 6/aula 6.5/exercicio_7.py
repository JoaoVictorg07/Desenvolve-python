import random

# Gerar uma lista aleatória de 20 elementos
lista = [random.randint(1, 100) for i in range(20)]

def dividir_lista(lista, tamanho):
    # Usar compreensão de lista para dividir a lista original
    return [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]

# Exibir a lista original
print("Lista original:")
print(lista)

while True:
    # Solicitar o tamanho para divisão
    tamanho = int(input("Tamanho para divisão (ou 0 para sair): "))

    if tamanho == 0:
        print("Encerrando o programa.")
        break
    
    # Dividir a lista conforme o tamanho informado
    sublistas = dividir_lista(lista, tamanho)

    # Exibir as sublistas
    print(f"Sublistas: {sublistas}")
