D1 = int(input())
D2 = int(input())
D3 = int(input())
D4 = int(input())

if D1<D2 and D2<D3 and D3<D4:
    print('Fish Rising')
elif D1>D2 and D2>D3 and D3>D4:
    print('Fish Diving')
elif D1==D2 and D2==D3 and D3==D4:
    print('Fish At Constant Depth')
else:
    print('No Fish')