import random

def encrypt(lista):
    # Gerar a chave de criptografia aleatória entre 1 e 10
    chave = random.randint(1, 10)

    # Função auxiliar para criptografar um único caractere
    def criptografar_caractere(c, chave):
        # Verificar se o caractere está dentro do intervalo visível (33 a 126)
        if 33 <= ord(c) <= 126:
            # Aplicar a cifra de substituição com a chave e manter no intervalo 33-126
            return chr(33 + (ord(c) - 33 + chave) % 94)
        return c  # Se estiver fora do intervalo, retorna o caractere sem alteração

    # Criptografar cada string da lista
    lista_criptografada = []
    for string in lista:
        string_criptografada = ''.join(criptografar_caractere(c, chave) for c in string)
        lista_criptografada.append(string_criptografada)

    return lista_criptografada, chave

# Exemplo de uso:
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave_criptografia = encrypt(nomes)

print(f"Nomes criptografados: {nomes_criptografados}")
print(f"Chave de criptografia: {chave_criptografia}")
