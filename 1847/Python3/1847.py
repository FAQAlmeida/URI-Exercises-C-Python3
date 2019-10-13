a, b, c = map(int, input().split())

if a > b:
    if b <= c:
        resp = ':)'
    elif b > c and a - b > b - c:
        resp = ':)'
    elif b > c and a - b <= b - c:
        resp = ':('
elif a < b:
    if b >= c:
        resp = ':('
    elif b < c and b - a > c - b:
        resp = ':('
    elif b < c and b - a <= c - b:
        resp = ':)'
else:
    if b >= c:
        resp = ':('
    else:
        resp = ':)'
print(resp)