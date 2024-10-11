def contagem_caracteres(s):
    # Inicializa um dicionário para armazenar a contagem de caracteres
    contagem = {}
    
    # Itera sobre cada caractere na string
    for caractere in s:
        if caractere in contagem:
            contagem[caractere] += 1  # Incrementa a contagem se o caractere já estiver no dicionário
        else:
            contagem[caractere] = 1  # Adiciona o caractere ao dicionário com contagem inicial de 1
            
    return contagem

# Exemplo de uso
string_exemplo = "programacao"
resultado = contagem_caracteres(string_exemplo)

# Imprimindo o resultado
print(resultado)
