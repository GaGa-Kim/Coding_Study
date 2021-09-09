import math
D, H, W = map(int, input().split())
r = math.sqrt(H*H+W*W)
print(int(D*H/r),int(D*W/r))
