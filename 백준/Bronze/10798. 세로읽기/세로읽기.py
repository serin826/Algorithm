words = [input() for i in range(5)]

for col in range(15):
    for row in range(5):
        if col < len(words[row]):
            print(words[row][col], end = '')