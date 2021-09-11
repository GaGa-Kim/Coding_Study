S, M = map(int, input().split())
if S+M < 0 or S-M < 0 or (S+M)%2 != 0:
    print(-1) 
else:
    A = (S+M)//2
    B = S-A
    print(max(A, B), min(A, B))