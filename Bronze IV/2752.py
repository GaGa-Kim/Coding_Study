n1, n2, n3 = map(int, input().split())
N = [n1, n2, n3]
N.sort()

for n in N:
    print(n, end=" ")