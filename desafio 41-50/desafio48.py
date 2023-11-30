print('\033[31m -=-'*16)
print(' '*15,'\033[1;97m SOMA DOS ÍMPARES MULTIPLOS DE 3')
print('\033[31m -=-\033[m'*16)
i=int(input('Qual o 1º número? '))
f=int(input('Qual o 2º número? '))
soma=0
cont=0
if i%2==0:
    for c in range(i+1, f+1, 2):
        if c%3==0:
            print(c, end=' ')
            soma+=c
            cont+=1
else:
    for c in range(i, f+1, 2):
        if c%3==0:
            print(c, end=' ')
            soma+=c
            cont+=1
print(f'\nA soma de todos os {cont} valores é {soma}')
print('\033[36mSLOTOV AGRADECE!\033[m')
