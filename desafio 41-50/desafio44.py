print('\033[31m -=-'*16)
print(' '*19,'\033[1;97m CÁLCULO DO PAGAMENTO')
print('\033[31m -=-\033[m'*16)
precodprod= float(input('Qual o valor do produto? '))
formqdpaga= int(input('Qual a forma de pagamento?\n [1] Á VISTA\n [2] CARTÃO 1X\n [3] CARTÃO 2X\n [4] CARTÃO 3X OU MAIS\nDIGITE A SUA OPÇÃO DE PAGAMENTO: '))
if formqdpaga==1:
    print(f'O valor final do seu produto ficou de: {precodprod-precodprod*(10/100)}')
elif formqdpaga==2:
    print(f'O valor final do seu pagamento ficou de: {precodprod-precodprod*(5/100)}')
elif formqdpaga==3:
    print(f'O valor final do seu pagamento ficou de: {precodprod}')
elif formqdpaga==4:
    print(f'O valor final do seu pagamento ficou de: {precodprod+precodprod*(20/100)}')
else:
    print('\033[31mCOMANDO IVÁLIDO\033[m')
print('\033[36mSLOOTOV AGRADECE!\033[m')