n, h, v = map(int, input().split())
c1 = 4 * h * v
c2 = 4 * (n-v) * h
c3 = 4 * (n-h) * v
c4 = 4 * (n-h) * (n-v)
print(max(c1, c2, c3, c4))