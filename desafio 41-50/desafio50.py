print('\033[31m -=-'*16)
print(' '*20,'\033[1;97m SOMA DOS PARES')
print('\033[31m -=-\033[m'*16)
soma=0
for c in range (1,7):
    n=int(input('Digite um número: '))
    if n%2==0:
        soma=soma+n
print(f'A soma dos valores pares digitados é {soma}')
print('\033[36m SLOTOV AGRADECE!\033[m')
