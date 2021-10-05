import math
w, h = map(int, input().split())
a = math.sqrt(w**2 + h**2)
print(w+h-a)
