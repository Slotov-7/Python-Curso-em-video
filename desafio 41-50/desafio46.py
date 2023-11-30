import time
print('\033[31m -=-'*16)
print(' '*20,'\033[1;97m CONTAGEM REGRESSIVA')
print('\033[31m -=-\033[m'*16)
i=int(input('Com qual valor gostaria de iniciar a contagem? '))
f=int(input('Com qual valor gostaria de finalizar a contagem? '))
for c in range (i, f-1, -1):
    print(c)
    time.sleep(1)
print('FIM!')
print('\033[36mSLOTOV AGRADECE\033[m')
