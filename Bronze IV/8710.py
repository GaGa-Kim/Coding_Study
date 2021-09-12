import math
k, w, m = map(int, input().split())
h = w-k
print(math.ceil(h/m))