k = int(input())
total = 25 + k * 0.01
if total < 100:
    total = 100.00
elif total >= 2000:
    total = 2000.00
print("%0.2f" %total)