#método string - inconsistente devido utilização de uma lista (vetor) não conseguir entebder quando não há 4 digitos
# numero=str(input('Digite um numero: '))
# num=numero
# print('Analisando o numero .. {}'.format(num))
# print('A milhar é: {}'.format(num[0]))
# print('A centena é: {}'.format(num[1]))
# print('A dezena é: {}'.format(num[2]))
# printnt('A unidade é: {}'.format(num[3]))

#método matemáitco, eficiente porem com o código "feio"
numero=int(input('Digite um numero: '))
u=numero // 1 %10 #para separarmos a unidade, dividimos por 1 (divisão inteira) e pegamos o resto da divisão por 10
d=numero //10 %10 #para separarmos a unidade, dividimos por 10 (divisão inteira) e pegamos o resto da divisão por 10
c=numero // 100 %10 #para separarmos a unidade, dividimos por 100 (divisão inteira) e pegamos o resto da divisão por 10
m=numero // 1000 %10 #para separarmos a unidade, dividimos por 1000 (divisão inteira) e pegamos o resto da divisão por 10
print('Analisando o numero .. {}'.format(numero))
print('A milhar é: {}'.format(m))
print('A centena é: {}'.format(c))
print('A dezena é: {}'.format(d))
print('A unidade é: {}'.format(u))