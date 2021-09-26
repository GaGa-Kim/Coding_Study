By, Bm, Bd = map(int, input().split())
Ty, Tm, Td = map(int, input().split())

if Bm < Tm:
    age = Ty - By
elif (Bm == Tm) and (Bd <= Td):
    age = Ty - By
else:
    age = Ty - By -1
print(age)
print(Ty - By + 1)
print(Ty - By)
