import string

def eh_palindromo(frase):
    # Remove espaços e pontuação, e converte tudo para minúsculas
    frase_limpa = ''.join([letra.lower() for letra in frase if letra.isalnum()])
    
    # Verifica se a frase é igual a ela mesma invertida
    return frase_limpa == frase_limpa[::-1]

# Loop principal do programa
while True:
    # Solicita a frase do usuário
    frase = input("Digite uma frase (ou 'Fim' para encerrar): ")
    
    # Verifica se o usuário quer encerrar o programa
    if frase.lower() == "fim":
        print("Programa encerrado.")
        break
    
    # Verifica se a frase é um palíndromo
    if eh_palindromo(frase):
        print("A frase é um palíndromo!")
    else:
        print("A frase não é um palíndromo.")
