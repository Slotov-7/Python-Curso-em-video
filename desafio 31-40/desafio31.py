from math import ceil
vkm=float(input('Quantos Km são a sua viagem? '))
if vkm<=200:
    print('O valor da sua passagem é {}'. format(ceil(vkm*0.65)))
else:
    print('O valor da sua passagem é {}'.format(ceil(vkm*0.5)))
print('Tenha uma boa viagem!')