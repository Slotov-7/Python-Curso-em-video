from random import randint
itens=('Nada', 'ÍMPAR', 'PAR', '')
print('\033[31m -=-'*16)
print(' '*16,'\033[1;97m VAMOS JOGAR: ÍMPAR OU PAR')
print('\033[31m -=-\033[m'*16)
jogador=cont=0
while True:
    jogador=int(input('VOCÊ ESCOLHE ÍMPAR OU PAR?\n[1] ÍMPAR\n[2] PAR\nDIGITE SUA OPÇÃO: '))
    while jogador!=1 and jogador!=2:
        print('\033[33mcomando invalido\033[m')
        jogador=int(input('VOCÊ ESCOLHE ÍMPAR OU PAR?\n[1] ÍMPAR\n[2] PAR\nDIGITE SUA OPÇÃO: '))
    if jogador==1:
        pc=2
    if jogador==2:
        pc=1
    print(f'O jogador escolheu {itens[jogador]} e o pc escolheu {itens[pc]}')
    jn=int(input('Digite um número entre 1-10: '))
    pcn=randint(1,10)
    jpcn=jn+pcn
    if jpcn%2==0 and jogador==2:
        print('\033[32mJOGADOR GANHOU\033[m')
        cont+=1
        soma=jpcn
        print(f'Você jogou {jn} e o pc jogou {pcn} a soma é igual a {soma}, que é um número par')
    if jpcn%2==1 and jogador==1:
        print('\033[32mJOGADOR GANHOU\033[m')
        cont+=1
        soma=jpcn
        print(f'Você jogou {jn} e o pc jogou {pcn} a soma é igual a {soma}, que é um número ímpar')
    if jpcn%2==1 and pc==1:
        print('\033[34mPC GANHOU\033[m')
        soma=jpcn
        print(f'Você jogou {jn} e o pc jogou {pcn} a soma é igual a {soma}, que é um número ímpar')
        break
    if jpcn%2==0 and pc==2:
        print('\033[34mPC GANHOU\033[m')
        soma=jpcn
        print(f'Você jogou {jn} e o pc jogou {pcn} a soma é igual a {soma}, que é um número par')
        break
print(f'Você ganhou {cont} vezes consecutivas')
print('\033[36mSLOTOV AGRADECE!\033[m')
