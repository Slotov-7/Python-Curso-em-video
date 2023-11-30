print('\033[31m -=-'*16)
print(' '*19,'\033[1;97m CONVERSOR DE BASES ')
print('\033[31m -=-\033[m'*16)
num=int(input('Digite um número inteiro: '))
opcao=int(input('Gostaria de converter para qual base?\n[1] Binario\n[2] Octal\n[3] Hexadecimal\nDigite a opção desejada: '))
if opcao==1:
    print('O número {} em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao==2:
    print('O número {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao==3:
    print('O número {} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('\033[107;30mOpção invalida\033[m')
