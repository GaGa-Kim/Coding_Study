A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

S1 = min(A, B, C, D)
S2 = max(E, F)
SUM = A+B+C+D-S1+S2
print(SUM)