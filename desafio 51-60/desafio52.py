print('\033[31m -=-'*16)
print(' '*25,'\033[1;97m É PRIMO?')
print('\033[31m -=-\033[m'*16)
n= int(input('Digite um número: '))
tot=0
for c in range(1, n+1):
    if n%c==0:
        print('\033[34m', end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
if tot==2:
    print(f'\n\033[mO número {n} é primo')
else: 
    print(f'\n\033[mO número {n} não é primo')
print('\033[36mSLOTOV AGRADECE!\033[m')