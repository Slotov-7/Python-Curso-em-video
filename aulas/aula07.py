n1=int(input('Qual o 1º valor?'))
n2=int(input('Qual o 2º valor?'))
s=n1+n2
m=n1*n2
d=n1/n2
su=n1-n2
di=n1//n2
p=n1**n2
rd=n1%n2
print('A soma é igual a {} e a subtração é igual a {}'.format(s,su))
print('A multiplicação é igual a {} e a pontência é igual a {}'.format(m,p))
print('A divisão é igual a {:.2f}, a divisão inteira é igual a {} e o resto da divisão é {}'.format(d,di,rd))