from datetime import date
f_date = date(2023, 11, 1)
l_date = date(2023, 11, 11)
delta = l_date - f_date
print(delta.days)