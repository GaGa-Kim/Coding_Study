A, B, C = map(int, input().split())
i = 1
while(True):
    C = C - A
    if i % 7 == 0:
        C = C - B
    if C <= 0:
        break
    i = i + 1
print(i)