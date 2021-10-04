a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input()) 
if T <= 30:
    p1 = a 
else:
    p1 = a + x*(T-30) * 21

if T <= 45:
    p2 = b
else:
    p2 = b + y*(T-45) * 21

print(p1, p2)