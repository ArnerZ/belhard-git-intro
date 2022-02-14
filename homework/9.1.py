from datetime import datetime

Now = datetime.now()
NewYear = datetime(day=1, month=1, year=2023)

timedelta = NewYear - Now
print("До Нового Года" ,timedelta)

