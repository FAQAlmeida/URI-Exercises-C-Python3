gas = 0
et = 0
die = 0

while True:
    t = int(input())
    if t == 2:
        gas += 1
    elif t == 1:
        et += 1
    elif t == 3:
        die += 1
    elif t == 4:
        break
print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(et,gas,die))