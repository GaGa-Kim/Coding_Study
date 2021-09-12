A = int(input())
B = int(input())
C = B-A

if C<=0:
    print('Congratulations, you are within the speed limit!')
elif C>=1 and C<=20:
    print('You are speeding and your fine is $100.')
elif C>=21 and C<=30:
    print('You are speeding and your fine is $270.')
elif C>=31:
    print('You are speeding and your fine is $500.')
