import datetime as dt
now = dt.datetime.now()
born = dt.datetime(2006, 9, 25)
age = now - born
print(age)