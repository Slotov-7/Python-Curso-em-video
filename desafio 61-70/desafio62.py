print('\033[31m -=-'*16)
print(' '*20,'\033[1;97m TERMOS DE UMA PA 3.0')
print('\033[31m -=-\033[m'*16)
pri=int(input('Qual o 1º termo da PA ? '))
r=int(input('Qual a razão da PA? '))
ult=int(input('Quantos termos você quer nessa PA?  '))
termo=pri
cont=1
mais=1
while mais!=0: 
    while cont <=ult:
        print(f'{termo};', end=' ')
        termo+=r
        cont+=1
    print(f'\nEssa é a PA desejada com {ult} termos')
    mais=int(input('Quantos termos a mais você quer? '))
    ult+=mais
print('\033[36mSLOTOV AGRADECE!\033[m')