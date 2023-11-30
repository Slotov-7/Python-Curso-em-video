print('\033[31m -=-'*16)
print(' '*19,'\033[1;97m CALCULADOR DE IMC ')
print('\033[31m -=-\033[m'*16)
peso= float(input('Qual o seu peso em KG ? '))
altura=float(input('Qual a sua altura em M? '))
imc= peso/altura**2
print(f'Seu IMC é {imc:.2f}')
if imc<18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5<=imc<25:
    print('Você está no PESO IDEAL')
elif 25<=imc<30:
    print('Você está SOBREPESO ')
elif 30<=imc<=40:
    print('Você está com OBESIDADE')
elif imc>40:
    print('Você está com OBSIDADE MÓRBIDA')
print('\033[36mSLOTOV AGRADECE!\033[m')