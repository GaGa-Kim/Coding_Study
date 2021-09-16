T = int(input())
A, B, C, D, E = map(int, input().split())
list = [A, B, C, D, E]

count = 0
for i in range(len(list)):
    if list[i] == T:
        count = count + 1
print(count)