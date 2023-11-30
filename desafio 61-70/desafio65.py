print('\033[31m -=-'*16)
print(' '*21,'\033[1;97mMENOR E MAIOR VALOR')
print('\033[31m -=-\033[m'*16)
cont=1
nova=''
soma=media=quant=maior=menor=0
media
while nova!='N':
    n=int(input(f'Digite o {cont}º valor: '))
    quant+=1
    cont+=1
    if quant==1:
        menor=maior=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    nova=str(input('Quer continuar? [S/N] ')).upper()
    soma+=n
media=soma/quant
print(f'Você digitou {quant} números e média foi {media:.2f}. ')
print(f'O maior número digitado foi {maior} e o menor número digitado foi o {menor}. ')
print('\n\033[36mSLOTOV AGRADECE!\033[m')
