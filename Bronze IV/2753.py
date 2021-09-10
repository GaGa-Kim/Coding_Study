Y = int(input())
if Y%4==0 & Y%100==0:
    print(1)
elif Y%400==0:
    print(1)
else:
    print(0)