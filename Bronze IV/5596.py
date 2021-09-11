S1 = list(map(int, input().split()))
S2 = list(map(int, input().split()))

sum1 = 0
for i in range(len(S1)):
    sum1 += S1[i]

sum2 = 0
for j in range(len(S2)):
    sum2 += S2[j]

if sum1 > sum2:
    print(sum1)
elif sum1 == sum2:
    print(sum1)
else:
    print(sum2)