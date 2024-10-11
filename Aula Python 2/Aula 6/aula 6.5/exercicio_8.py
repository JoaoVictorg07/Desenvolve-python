def avalia_tabuleiro(tabuleiro):
    # Verificar as linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return f"Vencedor: {linha[0]}"

    # Verificar as colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != ' ':
            return f"Vencedor: {tabuleiro[0][col]}"

    # Verificar a diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return f"Vencedor: {tabuleiro[0][0]}"

    # Verificar a diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return f"Vencedor: {tabuleiro[0][2]}"

    # Verificar se há espaços vazios, se não, é empate
    for linha in tabuleiro:
        if ' ' in linha:
            return "Jogo em andamento"

    return "Empate"

# Exemplo de uso:
tabuleiro1 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]

tabuleiro2 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['X', ' ', 'X']
]

tabuleiro3 = [
    ['X', 'X', 'O'],
    ['O', 'O', 'X'],
    ['X', 'O', 'X']
]

print(avalia_tabuleiro(tabuleiro1))  # Vencedor: X
print(avalia_tabuleiro(tabuleiro2))  # Vencedor: O
print(avalia_tabuleiro(tabuleiro3))  # Empate
