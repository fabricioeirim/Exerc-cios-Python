nome = str(input('Digite seu nome completo: ')).strip()
print('Olá, prazer em te conhecer')
nomea=nome.split()
print('O seu primeiro nome é {}'.format(nomea[0]))
print('O seu ultimo nome é {}'.format(nomea[len(nomea)-1]))

