print('\033[31m -=-'*16)
print(' '*19,'\033[1;97m CALCULADOR DE MÉDIA? ')
print('\033[31m -=-\033[m'*16)
n1=float(input('Qual a 1° nota? '))
n2=float(input('Qual a 2° nota? '))
n3=float(input('Qual a 3° nota? '))
n4=float(input('Qual a 4° nota? '))
m= (n1+n2+n3+n4)/4
print('Sua média foi {:.1f}'. format(m))
if m<5:
    print('\033[31mVOCÊ ESTÁ REPROVADO!\033[m')
elif 7>m>5:
    print('\033[34mVOCÊ FICOU DE RECUPERÇÃO\033[m')
elif m>7:
    print('\033[32mVOCÊ FOI APROVADO\033[m')
print('\033[36mA ESCOLA SLOTOVS AGRADECE!\033[m')
