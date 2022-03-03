import random
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do outro aluno: '))
n3 = str(input('Digite o nome do outro aluno: '))
n4 = str(input('Digite o nome do outro aluno: '))
lista = [n1,n2,n3,n4]
print('O aluno escolhido para apagar o quadro foi {}: '.format(random.choice(lista)))

