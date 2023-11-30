nome=input('Qual o seu nome completo? ')
n= nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu útimo nome é: {}'.format(n[len(n)-1]))