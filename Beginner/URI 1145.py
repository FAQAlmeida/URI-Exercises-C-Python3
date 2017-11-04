a, b = map(int,input().split())
for x in range(1, b + 1):
    if x % a != 0:
        print(x, end=' ')
    elif x % a == 0:
        print(x)