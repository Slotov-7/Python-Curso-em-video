print('\033[31m -=-'*16)
print(' '*16,'\033[1;97m ANALISANDO OS DADOS DO GRUPO')
print('\033[31m -=-\033[m'*16)
cont=contida=conthom=contm20=0
while True:
    cont+=1
    idade=int(input(f'Qual a idade {cont}ª pessoa? '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input(f'Qual o sexo {cont}ª pessoa? [M/F] ')).strip().upper()[0]
    if idade>18:
        contida+=1
    if sexo=='M':
        conthom+=1
    if sexo=='F' and idade<20:
        contm20+=1
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp=='N':
        break
print(f'{conthom} pessoa (s) é (são) homem (ns)')
print(f'{contida} pessoa (s) possue (em) mais de 18 anos')
print(f'{contm20} pessoa (s) é (são) mulher (es) com menos de 20 anos')
print('\033[36mSLOTOV AGRADECE!\033[m')
