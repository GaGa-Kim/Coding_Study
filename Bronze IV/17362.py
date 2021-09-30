n = int(input())
m = n % 8
if m == 1:
    print(1)
elif m == 2 or m == 0:
    print(2)
elif m == 3 or m == 7:
    print(3)
elif m == 4 or m == 6:
    print(4)
elif m == 5:
    print(5)

