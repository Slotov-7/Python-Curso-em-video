print('\033[31m -=-'*16)
print(' '*18,'\033[1;97m SIMULADOR DE EMPRÉSTIMO ')
print('\033[31m -=-\033[m'*16)
casa=float(input('Qual o valor do imovél em R$? '))
salario=float(input('Qual o valor do seu salário em R$? '))
ano=int(input('Em quantos anos gostaria de pagar? '))
parcelam=casa/(ano*12)
sal30= salario*(30/100)
if parcelam<=sal30:
    print('Seu empréstimo foi aprovado! ')
    print('O valor da sua parcela é {:.2f}'.format(parcelam))
else:
    print('Seu emprétimo não pode ser aprovado. Sentimos muito!')
