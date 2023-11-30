print('\033[31m -=-'*16)
print(' '*20,'\033[1;97m TABUADA 2.0')
print('\033[31m -=-\033[m'*16)
n=int(input('De qual número deseja a tabuada? '))
f=int(input('Até que número gostaria? '))
for c in range (0,f+1):
    print(f'{n} x {c} = {n*c}')
print(f'ESSA É A TABUADA DO {n} ATÉ O {f}')
print('\033[36mSLOTOV AGRADECE!\033[m')