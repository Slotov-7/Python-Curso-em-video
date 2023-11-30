from datetime import date
print('\033[31m -=-'*16)
print(' '*17,'\033[1;97m JÁ ESTÁ MA HORA DE ME ALISTAR? ')
print('\033[31m -=-\033[m'*16)
anodnasc=int(input('Em qual ano você nasceu? '))
anoatual= date.today().year
idade= anoatual-anodnasc
if idade==18:
    print('Está na hora de fazer seu alistamento.')
elif idade<18:
    print('Falta {} ano (s) para você se alistar'.format(18-idade))
elif idade>18:
    print('Você deveria ter se alistado a {} ano(s) atrás'.format(idade-18))
print('\033[1;4;32mO Exercito Brasileiro agradece!\033[m')