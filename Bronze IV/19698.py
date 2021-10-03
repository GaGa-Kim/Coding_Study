N, W, H, L = map(int, input().split())
if (W*H)//(L*L) < N:
    print((W*H)//(L*L))
else:
    print(N)
