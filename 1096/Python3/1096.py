class main:
    j = 7
    a = 0
    i = 1
    cont = 0
    for b in range(5):
        while a <= 2:
            print('I={} J={}'.format(i,j))
            j -= 1
            a += 1
        a = 0
        j = 7
        i += 2