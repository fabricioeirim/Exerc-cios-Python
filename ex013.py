s = float(input('Digite o salario atual R$ '))
sn = s + (s*0.15)
print('O salario R${:.2f} reajustado em 15% passou a ser R${:.2f} no próximo mes'.format(s, sn))
