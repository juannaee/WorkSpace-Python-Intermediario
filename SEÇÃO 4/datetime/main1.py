from datetime import datetime
from pytz import timezone


data_1 = datetime(2023, 10, 30, 17, 10, 59)
print(data_1)


data_str = "2023-10-30 17:18:59"
data_str_formatter = "%Y-%m-%d %H:%M:%S"

data_2 = datetime.strptime(data_str, data_str_formatter)
print(data_2)

data_3 = datetime.now()
print(data_3)

data_4 = datetime.now(timezone("US/Eastern"))
print(data_4)
