a = int(input())
b = int(input())
soma = 0

if a < b:
    for x in range(a, b + 1):
        if x % 13 != 0:
            soma += x
else:
    for x in range(b, a+1):
        if x % 13 != 0:
            soma += x
print(soma)