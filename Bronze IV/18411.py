A, B, C = map(int, input().split())
list = [A, B, C]
list.sort(reverse=True)
print(list[0]+list[1])