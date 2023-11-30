print('\033[31m -=-'*16)
print(' '*22,'\033[1;97m COMPARADOR DE PESOS? ')
print('\033[31m -=-\033[m'*16)
maior=0
menor=0
for p in range(1,6):
    peso= float(input(f'Qual o peso da {p}º pessoa em KG? '))
    if p==1:
        maior=p
        menor=p
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print(f'O maior peso lido foi {maior}KG e o menor foi {menor}KG')
print('\033[36mSLOTOV AGRADECE!\033[m')