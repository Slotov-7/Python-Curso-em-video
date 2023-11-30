dia=input('Em que dia você nasceu?')
mes=input('E em qual mês?')
ano=input('E o ano?')
cores= {'limpa':'\033[m', 
        'azul':'\033[34m', 
        'vermelho':'\033[31m',
        'preto':'\033[30m',
        'cinza':'\033[37m'}
print(f'Você nasceu no dia {dia}, do mês de {mes}, e no ano de {ano}')
