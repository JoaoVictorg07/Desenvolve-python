import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        # Se a palavra tiver 3 ou menos letras, não é necessário embaralhar
        if len(palavra) <= 3:
            return palavra
        
        # Separa a primeira e a última letra
        primeira, ultima = palavra[0], palavra[-1]
        # Embaralha as letras internas
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        # Reconstroi a palavra com as letras embaralhadas
        return primeira + ''.join(meio) + ultima

    # Divide a frase em palavras, embaralha cada uma e junta de volta em uma frase
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in frase.split()]
    return ' '.join(palavras_embaralhadas)
