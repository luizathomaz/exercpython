matriz = [[], [], [], [], [], [], [], [], []]
num = 0
for c in range(0, 9):
    num = int(input(f'Digite o {c+1} número: '))
    matriz[c].append(num)
print(matriz)

#como o professor fez:
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}] '))
print('=-'*30)
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()'''