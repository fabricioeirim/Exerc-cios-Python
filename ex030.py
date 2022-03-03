numero=int(input('Digite um numero: '))
resto = numero %2
if resto == 0:
    print('O numero {} é par'.format(numero))
else:
    print('O numero {} é impar'.format(numero))
