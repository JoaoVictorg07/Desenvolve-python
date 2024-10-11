while True:
    # Lê a expressão do usuário
    expressao = input("Digite uma expressão (ou 'Fim' para encerrar): ")

    # Verifica se o usuário deseja encerrar o programa
    if expressao.strip().lower() == "fim":
        print("Calculadora encerrada.")
        break

    try:
        # Avalia a expressão usando apenas operações de adição e subtração
        resultado = eval(expressao, {"__builtins__": {}}, {})
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Erro na expressão: {e}")
