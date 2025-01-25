A, B = map(int, input().split())
C = int(input())

time = A * 60 + B + C
H = time // 60
M = time % 60

if H >= 24:
    H = H % 24
    print(H, M)
else:
    print(H, M)