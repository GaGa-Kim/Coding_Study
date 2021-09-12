D, H, M = map(int, input().split())

timef = D*24*60 + H*60 + M
times = 11*24*60 + 11*60 + 11
time = timef - times

if times > timef:
    print(-1)
else:
    print(time)
