frase= str(input('Digite sua frase: '))
f= frase.upper()
print('Possui {} letras A'.format(f.count('A')))
print('Aparece inicialmente na posição {}'.format(f.find('A')+1))
print('A última vez que a letra A aparece é na posição {}'.format(f.rfind('A')+1))
