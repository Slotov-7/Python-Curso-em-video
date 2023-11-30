l1=float(input('Qual o valor do primeiro lado do triângulo? '))
l2=float(input('Qual o valor do segundo lado do triângulo? '))
l3=float(input('Qual o valor do terceiro lado do triângulo? '))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Pode fomar um triãngulo') 
else:
    print('Não pode formar um triângulo')