inter  = 0
gremio = 0
count = 0
empate = 0
while True:
    a, b = map(int, input().split())
    count += 1
    if a > b:
        inter += 1
    elif b > a:
        gremio += 1
    elif a==b:
        empate += 1
    print('Novo grenal (1-sim 2-nao)')
    resp = input()
    if resp != '1':
        break

if gremio > inter:
    resp = 'Gremio venceu mais'
elif inter > gremio:
    resp = 'Inter venceu mais'
else:
    resp = 'Nao houve vencedor'
print('{} grenais\nInter:{}\nGremio:{}\nEmpates:{}\n{}'.format(count,inter,gremio,empate,resp))