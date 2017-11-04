vetor = list()
for x in range(10):
    vetor.append(int(input()))
for x in range(len(vetor)):
    if vetor[x] <= 0:
        vetor[x] = 1
for x in range(len(vetor)):
    print('X[{}] = {}'.format(x,vetor[x]))