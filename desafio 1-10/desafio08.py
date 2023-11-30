m=int(input('Qual o valor em metros quer converter?'))
km=m/1000
hm=m/100
dam=m/10
dm=m*10
cm=m*100
mm=m*1000
print('O valor digitado em metros {} é igual'.format(m))
print('o valor em quilômetros é {}, o valor em hectômetros é {} e o valor em decâmetro é {}'.format(km,hm,dam))
print('o valor em decímetro é {}, o valor em centímetro é {} e o valor em milímetro é {}'.format(dm,cm,mm))