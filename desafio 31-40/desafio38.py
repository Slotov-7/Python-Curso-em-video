print('\033[31m -=-'*16)
print(' '*19,'\033[1;97m COMPARADOR DE NÚMEROS')
print('\033[31m -=-\033[m'*16)
n1=float(input('Qual o 1° número? '))
n2=float(input('Qual o 2° número? '))
if n1>n2:
    print('O primeiro valor é maior')
elif n2>n1:
    print('O segundo valor é maior')
else:
    print('Os dois valores são iguais')