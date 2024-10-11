import random

def escolhe_palavra():
    """Lê o arquivo de palavras e escolhe uma aleatoriamente."""
    try:
        with open('gabarito_forca.txt', 'r', encoding='utf-8') as arquivo:
            palavras = arquivo.read().splitlines()
        return random.choice(palavras).upper()
    except FileNotFoundError:
        print("Arquivo 'gabarito_forca.txt' não encontrado.")
        return None

def carrega_enforcado():
    """Carrega os estágios do enforcado do arquivo."""
    try:
        with open('gabarito_enforcado.txt', 'r', encoding='utf-8') as arquivo:
            estagios = arquivo.read().split('\n\n')  # Divide os estágios em partes
        return estagios
    except FileNotFoundError:
        print("Arquivo 'gabarito_enforcado.txt' não encontrado.")
        return None

def imprime_enforcado(erros, estagios):
    """Imprime o estágio do enforcado correspondente ao número de erros."""
    print(estagios[erros])

def jogo_forca():
    palavra = escolhe_palavra()
    estagios = carrega_enforcado()

    if not palavra or not estagios:
        return

    # Variáveis de controle
    letras_adivinhadas = set()
    tentativas_restantes = 6
    progresso = ['_' for _ in palavra]

    print("Bem-vindo ao jogo da forca!")
    print(f"A palavra tem {len(palavra)} letras: {' '.join(progresso)}")

    # Loop do jogo
    while tentativas_restantes > 0 and '_' in progresso:
        letra = input("Digite uma letra: ").upper()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_adivinhadas.add(letra)

        if letra in palavra:
            # Atualiza o progresso com a letra encontrada
            for i, l in enumerate(palavra):
                if l == letra:
                    progresso[i] = letra
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            # Letra incorreta, decrementa tentativas e mostra o enforcado
            tentativas_restantes -= 1
            print(f"Ops! A letra '{letra}' não está na palavra.")
            imprime_enforcado(6 - tentativas_restantes, estagios)

        # Mostra o progresso atual
        print(" ".join(progresso))
        print(f"Tentativas restantes: {tentativas_restantes}\n")

    # Resultado final
    if '_' not in progresso:
        print(f"Parabéns, você acertou! A palavra era '{palavra}'.")
    else:
        print(f"Você perdeu! A palavra era '{palavra}'.")

# Executa o jogo
jogo_forca()
