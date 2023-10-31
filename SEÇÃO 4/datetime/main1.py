from datetime import datetime, timedelta
from pytz import timezone
from dateutil.relativedelta import relativedelta

data_1 = datetime(2023, 10, 30, 17, 10, 59)
print(data_1)


data_str = "2023-10-30 17:18:59"
data_str_formatter = "%Y-%m-%d %H:%M:%S"

data_2 = datetime.strptime(data_str, data_str_formatter)
print(data_2)

data_3 = datetime.now()
print(data_3)

data_4 = datetime.now(timezone("Asia/Tokyo"))
print(data_4)


data_5 = datetime(2023, 10, 30, 14, 20, 36, tzinfo=timezone("Asia/Tokyo"))
print(data_5)


fmt_1 = "%d/%m/%Y %H:%M:%S"
data_6 = datetime.strptime("31/10/2023 14:39:30", fmt_1)
data_7 = datetime.strptime("10/10/2023 14:39:30", fmt_1)
delta_1 = data_6 - data_7
delta_2 = timedelta(days=20)
print(data_7 - delta_2)
print(delta_1)
fmt_2 = "%d/%m/%Y %H:%M:%S"

data_8 = datetime.strptime("10/10/2001 15:35:26", fmt_2)
relative_delta_1 = data_8 - relativedelta(days=365 * 20)

print(relative_delta_1)

data_9 = datetime.now()
fmt_3 = "%d/%m/%Y"
print(data_9.strftime(fmt_3))
