s = 0
y = 0
for x in range(1,40,2):
    s += x/pow(2,y)
    y += 1
print('{:.2f}'.format(s))