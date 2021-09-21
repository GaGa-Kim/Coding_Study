s = input()
d = input()

start1 = s.split(':')
destination1 = d.split(':')

start2 = int(start1[0])*3600+int(start1[1])*60+int(start1[2])
destination2 = int(destination1[0])*3600+int(destination1[1])*60+int(destination1[2])

if start2 > destination2:
    destination2 = destination2 + 24*3600
print(destination2-start2)