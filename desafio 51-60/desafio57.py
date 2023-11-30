from datetime import date
print('\033[31m -=-'*16)
print(' '*22,'\033[1;97m VALIDADOR DE DADOS ')
print('\033[31m -=-\033[m'*16)
nome=str(input('Informe seu nome completo: '))
print(f'Nome: {nome} registrado com sucesso.')
sexo= str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo= str(input('Dados inválidos. Por favor, tente novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
anodnas=int(input('Informe seu ano de nascimento: '))
idade=date.today().year-anodnas
while idade<18:
    anodnas=int(input('Dados iválidos. Por favor tente novamente: '))
print(f'Idade: {idade} registrada com sucesso.')
print('\033[36mSLOTOV AGRADECE!\033[m')