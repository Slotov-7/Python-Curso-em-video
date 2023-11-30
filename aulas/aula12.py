nome=str(input('Qual oseu nome? ')).upper()
if nome=='GUILHERME':
    print('Que nome legal!')
elif nome=='PEDRO' or nome=='MARIA' or nome=='JOÃO':
    print('Seu nome é muito popular!')
else:
    print('seu nome é normal')
print('Tenha um bom dia, {}!'.format(nome.capitalize()))