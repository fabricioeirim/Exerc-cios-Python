velocidade=float(input('Em qual velocidade estava o veículo? '))
if velocidade >= 80:
    multa=(velocidade-80)*7
    print('Você excedeu o limute de velocidade e foi multado em {:.2f} reais'.format(multa))
else:
    print('Tenha um bom dia e dirija com segurança')