vda=float(input('Qual o valor da diaria do carro?'))
da=float(input('Quantos dias foram alugados?'))
kmp=float(input('Quantos Km foram percorridos?'))
vkm=float(input('Qual o valor por km percorrido?'))
vtd=vda*da
vpkm=kmp*vkm
vt=vtd+vpkm
print('Você pagará pelo aluguel {}R$ e pelo Km percorrido {}R$ e no total {}R$.'.format(vtd, vpkm, vt))