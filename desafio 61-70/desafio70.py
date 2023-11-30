print('\033[31m -=-'*16)
print(' '*16,'\033[1;97m ESTATÍSTICA DE PRODUTOS')
print('\033[31m -=-\033[m'*16)
total=cont1000=quant=menorvalor=0
produtobarato=' '
while True:
    produto=str(input('Nome do produto: '))
    preço=float(input('Preço do produto: '))
    total+=preço
    quant+=1
    if quant==1:
        menorvalor=preço
        produtobarato=produto
    else:
        if menorvalor>preço:
            menorvalor=preço
            produtobarato=produto
    if preço>=1000:
        cont1000+=1
    pros=' '
    while pros not in 'SN':
        pros=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pros=='N':
        break
print(f'O valor total \033[32m{total}\033[m')
print(f'\033[34m{cont1000}\033[m produtos custam 1000 R$ ou mais ')
print(f'O produto mais barato foi o \033[33m{produtobarato}\033[m custando \033[35m{menorvalor} R$\033[m')
print('\033[36mSLOTOV AGRADECE\033[m')