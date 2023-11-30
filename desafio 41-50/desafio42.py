print('\033[31m -=-'*16)
print(' '*25,'\033[1;97m TRIÂNGULOS ')
print('\033[31m -=-\033[m'*16)
l1=float(input('Qual o valor do primeiro lado do triângulo? '))
l2=float(input('Qual o valor do segundo lado do triângulo? '))
l3=float(input('Qual o valor do terceiro lado do triângulo? '))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Pode fomar um triãngulo') 
    if l1==l2 and l2==l3:
        print('O triângulo é EQUILÁTERO ')    
    elif l1!=l2!=l3!=l1:
        print('O triângulo é ESCALENO') 
    else:
        print('O triãngulo é ISÓCELES')
else:
    print('Não pode formar um triângulo')
print('\033[36mSLOTOV AGRADECE!\033[m')