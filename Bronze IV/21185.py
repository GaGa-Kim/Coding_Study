N = int(input())
if N % 2 == 1:
    print("Either")
else:
    if N // 2 % 2 == 0:
        print("Even")
    else:
        print("Odd")