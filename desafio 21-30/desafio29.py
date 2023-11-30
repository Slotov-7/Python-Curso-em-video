velo=float(input('Qual a velocidade do carro em Km/h? '))
if velo>80:
    print('Você foi multado. \nO valor da sua multa é de {:.2f}'.format((velo-80)*7))
else:
    print('Você não foi multado.')