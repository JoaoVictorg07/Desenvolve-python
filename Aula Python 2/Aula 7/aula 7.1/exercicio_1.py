def imprimir_nome_escalado(nome):

    for i in range(1, len(nome), +1):
        print(nome[:i])

nome = input("Digite um nome: ")
imprimir_nome_escalado(nome)