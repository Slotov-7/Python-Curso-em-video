from math import sqrt
c1= float(input('Qual o valor do primeiro cateto? '))
c2= float(input('Qual o valor do segundo cateto? '))
h= c1**2+c2**2
print('O valor da hipotenusa é {}'.format(sqrt(h)))