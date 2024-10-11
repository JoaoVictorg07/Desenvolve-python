nums = [19, 22, -10, 4, -2, -3, 5, 6, -17, -4, -1, 67, 98, 23, 61]

#quando visitar um número negativo
#inicio de uma fatia
#continuação de uma fatia

inicio_fatia_maior, tam_fatia_maior = 0, 0
inicio_fatia_atual, tam_fatia_atual = 0, 0

for i in range(len(nums)):
    if nums[i] < 0:
        tam_fatia_atual += 1
        if tam_fatia_atual == 1: #se estou iniciando nova fatia
            inicio_fatia_atual = i
    else: # if nums[i] >= 0
        if tam_fatia_atual > tam_fatia_maior:
            inicio_fatia_maior = inicio_fatia_atual
        tam_fatia_atual = 0

print(inicio_fatia_maior, tam_fatia_maior)
del nums[inicio_fatia_maior: inicio_fatia_maior+tam_fatia_maior]
print(nums)