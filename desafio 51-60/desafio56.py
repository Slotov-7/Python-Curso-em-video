print('\033[31m -=-'*16)
print(' '*22,'\033[1;97m ANALISADOR COMPLETO ')
print('\033[31m -=-\033[m'*16)
soma=0
maioridade=0
nomevelho=''
mulher20=0
for p in range (1,5):
    print('\033[31m -=-\033[m'*16)
    print(' '*26, f'\033[1m{p}º PESSOA:\033[m')
    print('\033[31m -=-\033[m'*16)
    nome=str(input(' Qual o nome? ')).capitalize().strip()
    idade=int(input(' Qual a idade? '))
    soma+=idade
    sexo=str(input(' Sexo M/F: ')).upper().strip()
    if p==1 and sexo=='M':
        maioridade=idade
        nomevelho=nome
    if sexo=='M' and idade>maioridade:
        maioridade=idade
        nomevelho=nome
    if sexo=='F' and idade<20:
        mulher20+=1
media=soma/4
print(f'A média da idade do grupo é {media:.1f}.') 
print(f'O homem mais velho é o {nomevelho} com {maioridade} anos.')
if mulher20==1:
    print('Apenas uma mulher tem 20 anos')
else:
    print(f'São {mulher20} mulheres com menos de 20 anos')
print('\033[31m -=-\033[m'*16)
print('\033[36mSLOTOV AGRADECE!\033[m')