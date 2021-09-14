a, b, c = map(int, input().split())
list = [a, b, c]
list.sort()

if list[0]**2 + list[1]**2 == list[2]**2:
    print(1)
elif list[0] == list[1] == list[2]:
    print(2)
else:
    print(0)
