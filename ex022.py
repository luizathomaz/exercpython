nome = str(input('Digite seu nome completo: ')).strip()
mais = nome.upper()
min = nome.lower()
sem_espaco = nome.replace(' ', '')
quant = nome.split()
print('O nome todo em maiúsculo é {}'.format(mais))
print('O nome todo em minúsculo é {}'.format(min))
print('O nome tem {} letras'.format(len(sem_espaco)))
print('O primeiro nome tem {} letras'.format(len(quant[0])))
