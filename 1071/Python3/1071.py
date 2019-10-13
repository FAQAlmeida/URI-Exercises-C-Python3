class main:
    a = int(input())
    b = int(input())
    c = a
    d = b
    resp = 0
    if(a > b):
        while (b < a):
            if(b % 2 != 0 & b != d):
                if(b != d):
                    resp += b
            b = b + 1
    if(a < b):
        while a < b:
            if(a % 2 != 0):
                if(a != c):
                    resp += a
            a = a + 1
    print('{}'.format(resp))