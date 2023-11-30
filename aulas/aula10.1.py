n1=float(input('Qual a primeira nota? '))
n2=float(input('Qual a segunda nota? '))
n3=float(input('Qual a terceira nota? '))
n4=float(input('Qual a quarta nota? '))
m= (n1+n2+n3+n4)/4
if m>=6:
    print('Você está detro da média.')
    print('Parabéns!')
else:
    print('Você não está na média.')
    print('Que pena!')
print('Sua média é: {:.1f}'.format(m))