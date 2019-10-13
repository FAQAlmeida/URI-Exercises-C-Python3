class main:
    dentro = 0
    fora = 0
    a = int(input())
    for cont in range(a):
        b = int(input())
        if(b <= 20 and b >= 10):
            dentro += 1
        else:
            fora += 1
    print('{} in\n{} out'.format(dentro,fora))