chess1 = list(map(int, input().split()))
chess2 = [1, 1, 2, 2, 2, 8]
result = []

for i in range(len(chess2)):
    result.append(chess2[i]-chess1[i])

for j in result:
    print(j, end=' ')