A, P = map(int,input().split())
P1 = A * 7
P2 = P * 13
if P1 > P2:
    print('Axel')
elif P2 > P1:
    print('Petra')
else:
    print('lika')