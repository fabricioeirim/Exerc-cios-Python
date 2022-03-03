valori=float(input('Qual o valor do imovel a ser adiquirido? '))
salario=float(input('Informe o salario do comprador: '))
tempo=int(input('Em quantos anos você quer financiar o imovel? '))
tempo*12
prest=valori/(tempo*12)
percent=(prest/salario)*100
print('Para compar um imovel de {:.2f}R$ em {} anos a prestação será de {:.2f}R$ '.format(valori, tempo, prest))
if percent < 30:
    print('Emprestimo consedido')
else:
    print('Emprestimo negado')
