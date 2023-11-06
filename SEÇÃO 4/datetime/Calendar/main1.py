import calendar

print(calendar.calendar(2023))
print(calendar.month(2023, 10))
primeiro_dia, ultimo_dia = calendar.monthrange(2023, 11)
print(calendar.day_name[primeiro_dia])
