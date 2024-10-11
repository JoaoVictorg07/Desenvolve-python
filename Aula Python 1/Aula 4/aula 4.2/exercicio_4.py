n = int(input("Digite o número de jogos: "))
vitória = 0
empate = 0
derrota = 0
pontuação = 0

for i in range(n):
    gols_pro, gols_contra = map(int, input(f"Digite o resultado do jogo {i+1} (gols do Galo e gols do oponente): ").split())

if gols_pro > gols_contra:
    vitória + 1
    pontuação += 3
elif gols_pro < gols_contra:
    derrota + 1
else:
    empate += 1
    pontuação += 1

    print(f"Vitórias: {vitória}")
    print(f"Empates: {empate}")
    print(f"Derrotas: {derrota}")
    print(f"Pontuação: {pontuação}")