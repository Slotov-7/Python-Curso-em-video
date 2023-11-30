print('\033[31m -=-'*16)
print(' '*22,'\033[1;97mMENU DE OPÇÕES')
print('\033[31m -=-\033[m'*16)
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
soma = n1+n2
mult = n1*n2
menu = 0
while menu != 5:
    menu = int(input('\n[1]SOMA\n[2]MULTIPLICAÇÃO\n[3]MAIOR NÚMERO\n[4]DIGITAR NOVOS NÚMEROS\n[5]SAIR DO MENU\nDigite a opção desejada: '))
    if menu == 1:
        print(f'A soma de {n1} e {n2} é igual a {soma}')
    elif menu == 2:
        print(f'O produto de {n1} e {n2} é igual a {mult}')
    elif menu == 3:
        if n1 > n2:
            print(f'O maior número é {n1} ')
        else:
            print(f'O maior número é {n2}')
    elif menu==4:
        n1=float(input('Digite o novo valor do 1º número: '))
        n2=float(input('Digite o novo valor do 2º número: '))
        soma=n1+n2
        mult=n1*n2
print('\033[36mSLOTOV AGRADECE!\033[m')