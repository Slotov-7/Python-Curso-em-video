from datetime import date
print('\033[31m -=-'*16)
print(' '*22,'\033[1;97m QUEM É DE MAIOR? ')
print('\033[31m -=-\033[m'*16)
cont1=0
cont2=0
for c in range(0,7):
    anonsc= int(input(f'Em qual ano a {c+1}º pessoa nasceu? '))
    if date.today().year-anonsc>18:
        cont1+=1
    else:
        cont2+=1
print(f'{cont1} pessoas são maiores de idade')
print(f'{cont2} pessoas são menores de idade')
print('\033[36mSLOTOV AGRADECE!\033[m')