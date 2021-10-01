m, n = map(int, input().split())

sat = []
for _ in range(m):
    sat2 = list(map(int, input().split()))
    sat.append(sat2)
 
if m < 8:
    print("unsatisfactory")
else:
    print("satisfactory")