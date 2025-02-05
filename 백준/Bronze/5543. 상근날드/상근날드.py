B = []
D = []

for b in range(3):
    buger = int(input())
    B.append(buger)

for d in range(2):
    drink = int(input())
    D.append(drink)

print(min(B)+min(D)-50)