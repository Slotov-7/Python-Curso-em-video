from math import sin, cos, tan,radians
a= float(input('digite um ângulo: '))
s= sin(radians(a))
c= cos(radians(a))
t= tan(radians(a))
print('O valor do sen é {:.4f} \nO valor do cos é {:.4f} \nO valor da tan é {:.4f}'.format(s,c,t))