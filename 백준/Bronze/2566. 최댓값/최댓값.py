A = []
MAX = []

for i in range(9):
    num = list(map(int, input().split()))
    A.append(num)
    MAX.append(max(num))
    m =  max(MAX)   
print(m)
print(MAX.index(m)+1, A[MAX.index(m)].index(m)+1)