N, M = map(int, input().split())
if M == 1 or M == 2:
    print('NEWBIE!')
elif M !=1 and M !=2 and M <= N:
    print('OLDBIE!')
else:
    print('TLE!')