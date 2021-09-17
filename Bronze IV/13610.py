X, Y = map(int, input().split())

i = 1
while(True):
    if Y * i - X * i >= X:
        i += 1
        break
    i += 1
print(i)