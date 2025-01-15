

while True:
    i1, i2 = map(int, input().split())
    if i1 == 0 and i2 == 0:
        break
    elif i1 > i2:
        if i1 % i2 == 0:
            print('multiple')
        else:
            print('neither')
    elif i1 < i2:
        if i2 % i1 == 0:
            print('factor')
        else:
            print('neither')
