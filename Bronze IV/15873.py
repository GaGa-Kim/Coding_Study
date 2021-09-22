AB = input()
if len(AB) == 2:
    print(int(AB[0])+int(AB[1]))
elif len(AB) == 4:
    print(20)
else:
    if int(AB[-1]) == 0:
        print(int(AB[0])+10)
    else:
        print(10+int(AB[-1]))