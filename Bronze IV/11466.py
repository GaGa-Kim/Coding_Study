h, w = map(int, input().split())
a, b = max(h, w), min(h, w)

if a/3 <= b:
    l1 = a/3
else:
    l1 = b
l2 = b/2
print(max(l1, l2))