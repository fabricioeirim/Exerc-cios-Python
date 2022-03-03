salario=float(input('Digite o valor do salário para verificar o aumento: '))
if salario > 1250:
    salarion=salario*1.10
else:
    salarion=salario*1.15
print('O novo salario é {:.2f}'.format(salarion))