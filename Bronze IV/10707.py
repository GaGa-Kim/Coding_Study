A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

P1 = A*P
if P <= C:
    P2 = B
else:
    P2 = B + (P-C)*D
print(min(P1, P2))