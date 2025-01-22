T = int(input())

for _ in range(T):
    num = list(map(int, input().split()))

    add = 0 
    min_num = float('inf')

    for i in range(7):
        if num[i] % 2 == 0:
            add += num[i]
            if num[i] < min_num:
                min_num = num[i]

    print(add, min_num)