vetor = list()
a = int(input())
for x in range(10):
    vetor.append(a)
    a *= 2
for x in range(len(vetor)):
    print('N[{}] = {}'.format(x,vetor[x]))