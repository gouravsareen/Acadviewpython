import datetime
d=datetime.strptime('%Y%m%d')
s=d.strftime('%m')
s0=datetime.strptime(s,'%m')
print(d.day)



