print('\033[31m -=-'*16)
print(' '*15,'\033[1;97m QUANTOS NÚMEROS PARES POSSUI?')
print('\033[31m -=-\033[m'*16)
import math
i=int(input('Qual o 1º n° da contagem? '))
f=int(input('Qual o último n° da contagem? '))
cont=0
if i%2==0:
    for c in range (i,f+1,2):
        cont+=1
        print (c, end=' ')
else: 
    for c in range (i+1,f+1,2):
        cont=cont+1
        print (c, end=' ')
print(f'\nExistem {cont} números pares')
print('\033[36mSLOTOV AGRADECE!\033[m')