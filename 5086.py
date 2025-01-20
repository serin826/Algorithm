# 마지막에 0 0 을 입력한 후 끝나는 거 무시하면 안됨

while True:
    i1, i2 = map(int, input().split()) 
    # 얘가 맨 앞으로 가면 계속 같은 숫자로 돌아감. 숫자를 계속 입력할 수 있도록 해야 함함 
    
    if i1 == 0 and i2 == 0:
        break
    # 둘 다 0이면 멈추기
    
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



# 정답
while True :
  a, b = map(int, input().split())
  if a == 0 and b == 0 :
    break
  if b % a == 0 :
    print("factor")
  elif a % b == 0 :
    print("multiple")
  else :
    print("neither")

# 숫자 크기 비교 없어도 a/b, b/a 이렇게 위치 바꿔서 0인 걸 판별하니깐 크기비교 없어도 됨