x1, y1, z1 = map(int, input().split())
x2, y2, z2 = map(int, input().split())

if x1 <= x2 and y1 <= y2 and z1 <= z2:
    print('A')
elif x1/2 <= x2 and y1 <= y2 and z1 <= z2: 
    print('B')
elif x1 > x2 and y1 <= y2 and z1 <= z2: 
    print('C')
elif x1 > x2 and y1/2 <= y2 and z1 <= z2:
    print('D')
elif x1 > x2 and y1 > y2 and z1 <= z2:
    print('E')