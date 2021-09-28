t, p = map(int, input().split())
if p > 20:
    minute = t/(100-p)
    minutes = (p-20)*minute + 20*2*minute
else:
    minute = t/(80 + (20-p)*2)
    minutes = 2*minute*p
print(minutes)