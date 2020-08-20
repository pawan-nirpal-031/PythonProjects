import time
import datetime as dt
#print(type(time.localtime(time.time())))

#print(dt.datetime.now())
def DateTime():
    today = dt.datetime(2020,8,17)
    DateTimeToday = dt.datetime(2020,8,18,1,29,30) #date and time objct today takes yy,mm,dd,hh,min,secs
    print(DateTimeToday)
    return today

print(DateTime().strftime("%f"))
