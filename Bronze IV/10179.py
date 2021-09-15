T = int(input())
for i in range(T):
    price = float(input())
    print("$%.2f" %(price*0.8))
    print("$%.02f" %round(price*0.8, 2))