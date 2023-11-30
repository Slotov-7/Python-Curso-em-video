from random import randint
import time
cont=1
pc=randint(0,10) #faz o pc escolher um numero
print('\033[31m -=-'*16)
print(' '*22,'\033[1;97m ADVINHADOR 2.0 ')
print('\033[31m -=-\033[m'*16)
print('Vou penser em um número tente adivinhar...')
player= int(input('Qual número pensei? ')) #jogador adivinha
print('PROCESSANDO...')
time.sleep(2)
while player!=pc:
    player=int(input('Você errou! Tente novamente.\nDigite um novo número: '))#JOGADOR TENTA NOVAMENTE
    cont+=1
    print('PROCESSANDO...')
    time.sleep(2)
if player==pc:
    print('Você acertou! Parabéns!')
print(f'Pensei no múmero {pc}!')
print(f'Para acertar você tentou {cont}x.')
print('\033[36mSLOTOV AGRADECE!\033[m')