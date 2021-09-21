Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

if Ca >= Cr:
    C = 0
else:
    C = Cr - Ca

if Ba >= Br:
    B = 0
else:
    B = Br - Ba

if Pa >= Pr:
    P = 0
else:
    P = Pr - Pa

print(C+B+P)
