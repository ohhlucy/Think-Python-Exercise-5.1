#Write a script that converts and reads epoch time to datetime

import time
epoch=time.time()

#60*60*24=86400
total_sec = epoch % 86400
#60*60
hours = int(total_sec/3600)
total_minutes = int(total_sec/60)
mins = total_minutes % 60
sec = int(total_sec % 60)

days=int(epoch/86400)

print("The Current time is",hours,':',mins,':',sec)
print("Days since epoch:", days)

# importing the required module
import datetime
import calendar

t = datetime.datetime(1971, 1, 1, 0, 0, 0)
print(calendar.timegm(t.timetuple()))

t = datetime.datetime(1971, 1, 1, 0, 0, 0)
print(calendar.timegm(t.timetuple()))
    
