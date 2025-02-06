num = []

for i in range(2):
    n = list(map(int, input().split()))
    num.append(n)

A = num[0][0] * num[1][1] + num[1][0] * num[0][1]  # 분자
B = num[0][1] * num[1][1]  # 분모

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

m = GCD(A, B)  # 최대공약수 구하기
print(A // m, B // m)  # 기약분수로 출력
