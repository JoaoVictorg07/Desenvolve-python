def formatar_numero(numero):
    # Verificar se o número tem 8 dígitos
    if len(numero) == 8:
        # Adicionar um 9 na frente
        numero = '9' + numero
        print(f"Número formatado: {numero[:5]}-{numero[5:]}")
    
    # Verificar se o número já tem 9 dígitos e se começa com 9
    elif len(numero) == 9 and numero[0] == '9':
        print(f"Número formatado: {numero[:5]}-{numero[5:]}")
    
    else:
        print("Número inválido ou sem necessidade de formatação.")

# Exemplo de uso:
numero_celular = input("Digite o número de celular (somente números): ")
formatar_numero(numero_celular)