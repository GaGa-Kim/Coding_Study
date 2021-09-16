import math
R, C, N = map(int, input().split())
cctv1 = math.ceil(R/N)
cctv2 = math.ceil(C/N)
print(cctv1*cctv2)
