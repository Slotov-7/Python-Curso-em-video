print('\033[31m -=-'*16)
print(' '*25,'\033[1;97mFATORIAL')
print('\033[31m -=-\033[m'*16)
num=int(input('Digite um número: '))
c=1
r=1
for c in range(1,num):
    c+=1
    r*=c
print(f'{num}! é igual a {r}')
print('\033[36mSLOTOV AGRADECE!\033[m')