import datetime

today = datetime.date.today()

userdate = input("Enter a date (dd/mm/yyyy): ")
date,month,year = userdate.split('/')

userdatetime = datetime.datetime(int(year),int(month),int(date)).date()

duration =  today-userdatetime
print(duration)
