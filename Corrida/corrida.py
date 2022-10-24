#Informar a distância e tempo da corrida
distancia = input('Informe a distância percorrida em KM: ')
tempo = input('Informe o tempo, formato HH:MM:SS : ')

#calculo do pace
from datetime import datetime
minutos = datetime.strptime(tempo, "%H:%M:%S").minute
hora = (datetime.strptime(tempo, "%H:%M:%S").hour)*60
segundos = (datetime.strptime(tempo, "%H:%M:%S").second)/60
var1 = (minutos + hora + segundos)/float(distancia)
num = float((var1 - int(var1))*60)/100
pace = int(var1) + num

#velocidade em km/h
velocidade_media = 60/pace

#velocidade em m/s
veloc_ms = velocidade_media / 3.6

#velocidade em milha por hora
veloc_milha = velocidade_media / 1.609

#alterando a formatação das casas decimais
n_formatado = "{:.2f}".format(pace)
v_formatado = "{:.2f}".format(velocidade_media)
ms_formatado = "{:.2f}".format(veloc_ms)
milha_formatado = "{:.2f}".format(veloc_milha)

#resultados
print('O pace da corrida é: ' + str(n_formatado)+ ' min/km')
print('A velocidade média é: ' + str(v_formatado) + ' km/h')
print('A velocidade média é: ' + str(ms_formatado) + ' m/s')
print('A velocidade média é: ' + str(milha_formatado) + ' milhas/h')
