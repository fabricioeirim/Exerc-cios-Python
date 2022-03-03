distancia=float(input('Qual a distancia em KM da sua viajem? '))
if distancia <= 200:
    valor=distancia*0.50
else:
    valor=distancia*0.45
print('A distancia da sua viajem é de {}KM e vai custar {:.2f} reais'.format(distancia, valor))