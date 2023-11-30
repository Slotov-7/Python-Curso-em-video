ano=int(input('Digite uma ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano digitado é bissexto.')
else:
    print('O ano digitado não é bissexto.')