print('\033[31m -=-'*16)
print(' '*18,'\033[1;97m SEQUÊNCIA DE FIBONACCI 1.0')
print('\033[31m -=-\033[m'*16)
n=int(input('Quantos termos deseja? '))
t1=0
t2=1
cont=3
if n==1:
    print(f'{t1};')
else:
    print(f'{t1}; {t2}; ',end='')
    while cont<=n:
        t3=t1+t2
        print(f'{t3}; ', end='')
        t1=t2
        t2=t3
        cont+=1
print('\n\033[36mSLOTOV AGRADECE!\033[m')
