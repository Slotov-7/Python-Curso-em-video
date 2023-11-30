#tuplas variaveis compstas... 
lanche= ('hambúrguer', 'suco', 'pizza', 'pudim')
for pos, c in enumerate (lanche):
    print(f'Comi {c} na posição {pos}')
for c in lanche:
    print(f'vou comer {c}')
for c in range(0, len(lanche)):
    print(f'Vou comer {lanche[c]} na posição {c}')
print(sorted(lanche)) #organiza em ordem seja númerica ou alfabetica
#tuplas podem ser deletadas atravez do comando 'del'