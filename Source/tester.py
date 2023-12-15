import datetime

from datetime import datetime, timedelta, date
employee_date = date(95,12,12)  # uses date class from datetime package to check for accurate dates
current_year = datetime.now()
age = current_year.year - employee_date.year

print(age)