p1 = input()
p2 = input()
p3 = input()
p4 = input()
p5 = input()
p6 = input()
play = [p1, p2, p3, p4, p5, p6]
count = 0
for i in play:
    if i == 'W':
        count += 1 
if count >= 5:
    print(1)
elif count >= 3:
    print(2)
elif count >= 1:
    print(3)
else:
    print(-1)