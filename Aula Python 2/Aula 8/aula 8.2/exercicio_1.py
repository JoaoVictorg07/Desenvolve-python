def calcula_area_perimetro(dimensoes):
    # Desempacotando a tupla em largura e comprimento
    largura, comprimento = dimensoes
    
    # Calculando a área
    area = largura * comprimento
    
    # Calculando o perímetro
    perimetro = 2 * (largura + comprimento)
    
    # Retornando os resultados
    return area, perimetro

# Exemplo de uso
dimensoes_terreno = (5, 10)  # largura: 5, comprimento: 10
area, perimetro = calcula_area_perimetro(dimensoes_terreno)
print(f"Área: {area}, Perímetro: {perimetro}")
