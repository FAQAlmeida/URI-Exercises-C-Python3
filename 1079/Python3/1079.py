class main:
    
    cont = int(input())
    resp = list(range(cont))
    for i in resp:
            a, b, c = input().split()
            resp[i] = (float(a) * 2 + float(b) * 3 + float(c) * 5) / 10
    for j in range(cont):
        print('{0:.1f}'.format(resp[j]))