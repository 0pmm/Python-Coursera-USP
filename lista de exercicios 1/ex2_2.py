sp = input("Por favor, entre com o número de segundos que deseja converter: ")
dias = int(sp) // 86400
sp_restante = int(sp) % 86400
horas = sp_restante // 3600
sp_restante = sp_restante % 3600
minutos = sp_restante // 60
segundos = sp_restante % 60
print(dias,"dias,", horas,"horas,", minutos,"minutos e", segundos,"segundos.")