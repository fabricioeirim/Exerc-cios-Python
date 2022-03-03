ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = (ca**2 + co**2)**(1/2)
print('O avalo da hipotenusa é {:.2f}, para o ca {:.2f} e o co {:.2f}'.format(h,ca,co))

# from math import hypot
# ca = float(input('Digite o valor do cateto adjacente: '))
# co = float(input('Digite o valor do cateto oposto: '))
# print('O valor da hipotenusa é {:.2f}, para o ca {:.2f} e o co {:.2f}'.format(hypot(ca,co),ca,co))