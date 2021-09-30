import math

A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())

W = A1 / P1
S = (math.pi * R1 ** 2) / P2

if W > S:
    print('Slice of pizza')
else:
    print('Whole pizza') 