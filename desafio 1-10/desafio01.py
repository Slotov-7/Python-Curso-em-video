nome=input('Qual o seu nome? ')
cores= {'limpa':'\033[m', 
        'azul':'\033[34m', 
        'vermelho':'\033[31m',
        'preto':'\033[30m',
        'cinza':'\033[37m'}
print('Seja bem vindo (a) {} {}'.format(cores['azul'], nome))