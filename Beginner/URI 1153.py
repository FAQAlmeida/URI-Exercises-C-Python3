n = int(input())

for x in range(n - 1, 0, -1):
    n *= x

print(n)