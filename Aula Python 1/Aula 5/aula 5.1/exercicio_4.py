from datetime import datetime

data_hora_atual = datetime.now()

data = data_hora_atual.strftime("%d/%m/%Y ")
hora= data_hora_atual.strftime("%H:%M:%S")

print(f"Data: {data}")
print(f"Hora: {hora}")
