import datetime
employee="1212121200"
y=int(employee[4:6])
m=int(employee[2:4])
d=int(employee[0:2])
print(y,m,d)
a=datetime.date(y,m,d)
print(a)
