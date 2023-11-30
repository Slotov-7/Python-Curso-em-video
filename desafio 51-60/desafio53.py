print('\033[31m -=-'*16)
print(' '*22,'\033[1;97m É PALÍNDROMO?')
print('\033[31m -=-\033[m'*16)
frase= str(input('Digite a sua frase: ')).strip().upper()
palavra=frase.split()
j=''.join(palavra)
inverso=''
for letra in range(len(j)-1, -1,-1 ):
    inverso+= j[letra]
if j==inverso:
    print('É palíndromo')
else:
    print('Não é palíndromo')
print('\033[36mSLOTOV AGRADECE!\033[m')