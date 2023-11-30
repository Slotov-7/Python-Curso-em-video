s=float(input('Qual o valor do salário em R$?'))
a=float(input('Qual o valor do aumento em %?'))
vda=s*(a/100)
vdsn=s+vda
print('O valor do aumento é {}R$ e o valor do salário com o aumento é {}R$.'.format(vda,vdsn))