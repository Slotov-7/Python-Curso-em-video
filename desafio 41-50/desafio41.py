from datetime import date
print('\033[31m -=-'*16)
print(' '*15,'\033[1;97m QUAL A SUA CATEGORIA NO CLUBE? ')
print('\033[31m -=-\033[m'*16)
anon=int(input('Qual a ano você nasceu? '))
anoa= date.today().year
idade=anoa-anon
print('Você tem {} anos'.format(idade))
if idade<=8:
    print('Sua categoria é MIRIM')
elif 9<idade<=14:
    print('Sua categoria é INFANTIL')
elif 14<idade<=18:
    print('Sua categoria é JUNIOR')
elif 19<idade<=24:
    print('Sua categoria é SÊNIOR')
elif 24<idade:
    print('Sua categoria é MASTER')
print('\033[36mO CLUBE SLOTOVS AGRADECE!\033[m')