from datetime import datetime

date1 = datetime(2023, 10, 21, 14, 30, 0)
date2 = datetime(2023, 10, 20, 12, 0, 0)

date3 = date2 - date1
print("Seconds difference: ", (date1.day * 24 * 60 * 60 + date1.hour * 60 * 60 + date1.minute * 60+ date1.second)-(date2.day * 24 * 60 * 60 + date2.hour * 60 * 60 + date2.minute * 60+ date2.second))
