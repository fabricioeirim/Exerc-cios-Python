nome = str(input('Digite o seu nome: ')).strip()
print('Analisando seu nome ...')
print('Seu nome em maiuscula é {}'.format(nome.upper()))
print('Seu nome em minuscula é {}'.format(nome.lower()))
print(len(nome.strip()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
nome = nome.split()
print('Seu primeiro nome é {} e tem {} letras '.format(nome[0],len(nome[0])))









