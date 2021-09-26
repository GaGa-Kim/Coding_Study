N = int(input())
if N<=0:
    print('divide by zero')
else:
    record = list(map(int, input().split()))
    mean_record = sum(record)/N
    expect_record = 0
    for i in range(N):
        expect_record += record[i]/N
    print("%0.2f" %(mean_record/expect_record))

