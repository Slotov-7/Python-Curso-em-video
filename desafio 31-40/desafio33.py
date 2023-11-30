a= int(input('Digite um número: '))
b= int(input('Digite um número: '))
c= int(input('Digite um número: '))
menor=a
#verificando o menor 
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
print('O menor valor digitado foi: {}'.format(menor))
#verificando o maior
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O maior valor digitado foi: {}'.format(maior))