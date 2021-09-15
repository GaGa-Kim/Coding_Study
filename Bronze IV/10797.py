D = int(input()) 
N1, N2, N3, N4, N5 = map(int, input().split())
Number = [N1, N2, N3, N4, N5]
sum = 0

for i in range(len(Number)):
    if Number[i] == D:
        sum = sum + 1
print(sum)