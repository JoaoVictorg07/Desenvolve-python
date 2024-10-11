def gerenciar_fila_balada():
    fila = []  # Lista para armazenar as tuplas (nome, idade)

    while True:
        nome = input("Digite o nome (ou 'fim' para encerrar): ")
        if nome.lower() == 'fim':  # Condição para encerrar a coleta de dados
            break
        idade = int(input(f"Digite a idade de {nome}: "))
        fila.append((nome, idade))  # Adiciona a tupla (nome, idade) à lista

    # Inicializando as tuplas para menores e maiores de idade
    menores_de_idade = ()
    maiores_de_idade = ()

    # Classificando os nomes com base na idade
    for nome, idade in fila:
        if idade < 18:
            menores_de_idade += (nome,)  # Adiciona nome à tupla de menores de idade
        else:
            maiores_de_idade += (nome,)  # Adiciona nome à tupla de maiores de idade

    # Imprimindo os resultados
    print("Menores de idade que não poderão entrar:", menores_de_idade)
    print("Maiores de idade que poderão entrar:", maiores_de_idade)

# Chama a função para executar o script
gerenciar_fila_balada()
