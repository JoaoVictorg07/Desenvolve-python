def testa_equilatero(t):
    if t[0] == t[1] and t[1] == t[2]:
        return True
    else:
        return False

triangulos = [[2,2,2], [3,4,5], [3,2,2],[4,4,4]]
equilateros = list(filter(testa_equilatero, triangulos))
print(equilateros)
