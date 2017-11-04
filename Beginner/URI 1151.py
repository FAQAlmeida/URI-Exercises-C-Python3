n1 = 0
n2 = 1

n = int(input())

print('0 1', end=' ')

for x in range(n - 2):
    if x != n - 3:
        print(n1 + n2, end=' ')
    else:
        print(n1 + n2)
    aux = n1
    n1 = n2
    n2 = aux + n2