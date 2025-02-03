def GCD(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b


for n in range(int(input())):
    A, B = map(int, input().split())
    print(GCD(A, B))