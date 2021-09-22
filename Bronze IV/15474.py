N, A, B, C, D = map(int, input().split())

if N%A != 0:
    X = (N//A+1)*B
else:
    X = (N//A)*B

if N%C != 0:
    Y = (N//C+1)*D
else:
    Y = (N//C)*D

print(min(X, Y))