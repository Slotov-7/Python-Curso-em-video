from random import randint
import time
itens=('Nada', 'PEDRA', 'TESOURA', 'PAPEL')
print('\033[31m -=-'*16)
print(' '*13,'\033[1;97m VAMOS JOGAR: PEDRA, PAPEL OU TESOURA')
print('\033[31m -=-\033[m'*16)
player=int(input(f'O que você deseja escolher:\n [1] PEDRA\n [2] TESOURA\n [3] PAPEL\nDIGITE A SUA OPÇÃO: '))
pc=randint(1,3)
if player!=1 and player!=2 and player!=3:
    print('\033[33mJOGADA INVÁLIDA!\033[m')
else:
    print('JO')
    time.sleep(2)
    print('KEM')
    time.sleep(2)
    print('PÔ!')
    time.sleep(1)
    print('\033[31m-=-\033[m'*16)
    print(f'PC jogou: {itens[pc]}\nJogador jogou: {itens[player]}')
    print('\033[31m -=-\033[m'*16)
    if pc==1: #pc joga PEDRA
        if player==1:
            print('\033[34mEMPATOU\033[m')
            print('\033[31m-=-\033[m'*16)
        elif player==2:
            print('\033[31mPC GANHOU!\033[m')
            print('\033[31m-=-\033[m'*16)
        elif player==3:
            print('\033[32mJOGADOR GANHOU!\033[m')
            print('\033[31m-=-\033[m'*16)
        else:
            print('\033[33mJOGADA INVÁLIDA!\033[m')
            print('\033[31m-=-\033[m'*16)
    elif pc==2: #pc joga TESOURA
        if player==1:
            print('\033[32mJOGADOR GANHOU\033[m')
            print('\033[31m-=-\033[m'*16)
        elif player==2:
            print('\033[34mEMPATOU!\033[m')
            print('\033[31m-=-\033[m'*16)
        elif player==3:
            print('\033[31mPC GANHOU!\033[m')
            print('\033[31m-=-\033[m'*16)
        else:
            print('\033[33mJOGADA INVÁLIDA!\033[m')
            print('\033[31m-=-\033[m'*16)
    elif pc==3: #pc joga PAPEL
        if player==1:
            print('\033[31mPC GANHOU!\033[m')
            print('\033[31m-=-\033[m'*16)
        elif player==2:
            print('\033[32mJOGADOR GANHOU!\033[m')
            print('\033[31m-=-\033[m'*16)
        elif player==3:
            print('\033[34mEMPATOU\033[m')
            print('\033[31m-=-\033[m'*16)
        else:
            print('\033[33mJOGADA INVÁLIDA!\033[m')
            print('\033[31m-=-\033[m'*16)
print('\033[36mSLOOTOV AGRADECE!\033[m')
