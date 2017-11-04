n = int(input())
o = input().upper()
matriz = [[0 for col in range(12)] for row in range(12)]

for row in range(12):
    for col in range(12):
        matriz[row][col] = float(input())
soma = 0
for row in range(12):
    soma += matriz[row][n]

if o == 'S':
    print(soma)
else:
    print('{:.1f}'.format(soma / 12))