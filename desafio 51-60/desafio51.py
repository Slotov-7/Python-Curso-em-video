print('\033[31m -=-'*16)
print(' '*20,'\033[1;97m TERMOS DE UMA PA')
print('\033[31m -=-\033[m'*16)
pri=int(input('Qual o 1º termo da PA ? '))
r=int(input('Qual a razão da PA? '))
ult=int(input('Até que termo você quer essa PA?  '))
cont=0
for c in range(pri, ult+1, r):
    print(f'{c};', end=' ')
    cont+=1
print(f'\nEssa PA tem {cont} termos')
print('\033[36mSLOTOV AGRADECE!\033[m')
