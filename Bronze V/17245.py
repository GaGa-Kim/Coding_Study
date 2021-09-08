a = list(map(int, input().split())) 
c = list(map(int, input().split())) 
b = [c[0]-a[2], c[1]//a[1], c[2]-a[0]]
for i in b:
    print(i, end=" ")