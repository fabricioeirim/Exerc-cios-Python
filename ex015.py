d = int(input('Por quantos dias o veiculo ficou locado ? '))
km = float(input('Quantos KM o veiculo rodou ? '))
custo = (km*0.15)+(d*60)
print('O veiculo rodou {:.2f}KM em {:1} dias, o valor ser pago é de R${:.2f}'.format(km,d,custo))