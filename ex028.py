import random

print('Tente adivinhar o numero que eu pensei')
num = random.randint(0,5)
numc=int(input('Digite o numero que eu pensei: '))
if numc == num:
    print('Você acertou o numero')
else:
    print('Errrrrooooooouuuu')


