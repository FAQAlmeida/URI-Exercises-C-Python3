n = int(input())
o = input().upper()
matriz = [[0 for col in range(12)] for row in range(12)]

for row in range(12):
    for col in range(12):
        matriz[row][col] = float(input())
if o == 'S':
    print(sum(matriz[n]))
else:
    print('{:.1f}'.format(sum(matriz[n]) / 12))