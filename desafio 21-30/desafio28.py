from random import randint
import time
pc=randint(0,5) #faz o pc escolher um numero
print('-=-'*18)
print('|Vou pensar em um número de 0 a 5. tente advinhar...|')
print('-=-'*18)
player= int(input('Qual número pensei? ')) #jogador adivinha
print('PROCESSANDO...')
time.sleep(5)
if player==pc:
    print('Você acertou! Parabéns!')
else:
    print('Você errou! Que pena!')
print('Pensei no número {}'.format(pc))