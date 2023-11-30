from random import shuffle 
n1=input('Qual o nome do 1º aluno? ')
n2=input('Qual o nome do 2º aluno? ')
n3=input('Qual o nome do 3º aluno? ')
n4=input('Qual o nome do 4º aluno? ')
l= [n1, n2, n3, n4]
shuffle(l)
print('A ordem será:', l)