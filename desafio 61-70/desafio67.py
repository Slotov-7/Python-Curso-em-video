import time
print('\033[31m -=-'*16)
print(' '*20,'\033[1;97m TABUADA 3.0')
print('\033[31m -=-\033[m'*16)
c=0
while True: 
    n=int(input('De qual número deseja a tabuada? Digite um número negativo para terminar. '))
    if n<0:
        break
    else:
        for c in range(10):
            c+=1
            print(f'{n} x {c} = {n*c}')
        print(f'Essa é a tabuada do {n}')
        time.sleep(1.2)
print('\033[36mSLOTOV AGRADECE!\033[m')
