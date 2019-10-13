array = list(map(int, input().split()))
a = array[0]
soma = 0
for x in range(1, len(array)):
    if array[x] > 0:
        b = array[x]
        break

for i in range(b):
    soma += (a + i)

print(soma)