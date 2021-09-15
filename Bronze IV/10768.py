M = int(input())
D = int(input())
if 2 < M <= 12:
    print('After')
elif M == 2:
    if D == 18:
        print('Special')
    elif D < 18:
        print('Before')
    else:
        print('After')
else:
    print('Before')