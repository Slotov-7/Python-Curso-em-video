p=float(input('Qual o valor do produdo em R$?'))
d=float(input('Qual o valor do desconto em %?'))
vdd=p*(d/100)
vcd=p-vdd
print('O valor do desconto é {}R$ e o valor do produto com o desconto é {}R$.'.format(vdd,vcd))
