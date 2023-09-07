from datetime import date, time, datetime, timedelta

today = date.today()
print(today)
new_date = date(1999, 12, 31)  # 날짜 지정 가능
print(new_date)

print(time(9))   # 시간 지정 가능
print(time(9, 2))
print(time(9, 2, 2))
print(time(9, 2, 2, 2222))

dt = datetime.now() # => datetime을 이용하면 한꺼번에 지정 가능
print(dt)

dt = datetime(2002, 10, 20, 14, 9, 12)
print(dt)

today = datetime.now()
print(today)
print(today + timedelta(days = 20))
print(today - timedelta(days = 20)) # days, hours, weeks 등 모두 가능

# time()
import time
now = time.time() # = 1977년 1월 1일 0시 0분 0초부터 경과한 시간을 초로 반환

# localtime
from time import localtime
now = localtime()
print(now)

# strftime
from time import strftime
now = strftime("%Y-%m-%d %H:%M") 
now = strftime("%Y년 %m월 %d일 %H시 %M분")    # 날짜와 시간을 포메팅
print(now)