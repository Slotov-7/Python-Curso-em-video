sal=float(input('Qual o valor do seu salário? '))
if sal>1250:
    salv= sal*(10/100)+sal
    aumento= salv-sal
    print('O valor novo do salário é: {} e aumento foi de {}'.format(salv, aumento))
if sal<=1250:
    salv= sal*(15/100)+sal
    aumento=salv-sal
    print('O valor novo do salário é: {} e aumento foi de {}'.format(salv, aumento))
print('Obrigado!')