x = int(input())
while True:
    z = int(input())
    if z > x:
        break

count = 0
soma = 0
while True:
    count += 1
    soma += x
    x+=1
    if soma > z:
        break

print(count)
