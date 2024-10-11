import string

def checa_panagrama(frase):
    # Converte a frase para minúsculas e cria um conjunto com as letras
    letras = set(frase.lower())
    
    # Conjunto com todas as letras do alfabeto
    alfabeto = set(string.ascii_lowercase)
    
    # Verifica se o conjunto de letras da frase contém todas as letras do alfabeto
    return alfabeto.issubset(letras)

# Exemplo de uso
frase1 = "A rápida raposa marrom salta sobre o cão preguiçoso."
frase2 = "Este texto não contém todas as letras."

print(checa_panagrama(frase1))  # Saída: True
print(checa_panagrama(frase2))  # Saída: False
