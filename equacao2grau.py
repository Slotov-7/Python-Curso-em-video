print('\033[31m -=-'*16)
print(' '*16,'\033[1;97m FUNÇÃO DO 2º GRAU')
print('\033[31m -=-\033[m'*16)
a= float(input('Digite o valor de A: '))
b= float(input('Digite o valor de B: '))
c= float(input('Digite o valor de C: '))
delta=b**2-4*a*c
deltarz= delta**(1/2)
x1= (-b+deltarz)/2*a
x2= (-b-deltarz)/2*a
print(f'O valor do delta é igual {delta}')
if delta<0:
    print('Não existe raizes reais para essa equação')
elif delta==0:
    print('Existe apenas uma única raiz')
    print(f'x é igual a: {x1}')
else: 
    print('Possui duas raizes diferentes')
    print(f'x1 é igual a: {x1}')
    print(f'x2 é igual a: {x2}')
print('\033[36mSLOTOV AGRADECE\033[m')
