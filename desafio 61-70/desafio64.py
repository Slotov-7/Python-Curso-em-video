print('\033[31m -=-'*16)
print(' '*23,'\033[1;97m SOMADOR')
print('\033[31m -=-\033[m'*16)
cont=1
n=1
soma=0
while True:
    if n!=999:
        n=int(input(f'Digite o {cont}º valor ou "999" para parar: '))
    if n==999:
        break
    soma+=n
    cont+=1
print(f'A soma dos {cont-1} números digitados é {soma}')
print('\n\033[36mSLOTOV AGRADECE!\033[m')

