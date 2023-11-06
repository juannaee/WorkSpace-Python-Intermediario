import calendar, locale


print(calendar.month(2023, 11))
locale.setlocale(locale.LC_ALL, "")
print(calendar.month(2023, 11))
