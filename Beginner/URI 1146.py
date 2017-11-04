a = True
while a:
    n = int(input())
    if n == 0:
        a = False
    else:
        for x in range(1,n+1):
            if x % n == 0:
                print(x)
            else:
                print(x,end=' ')