# 1 date defference
from datetime import datetime

def date_difference(date1, date2): 
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((date2 - date1).days)

print(date_difference('2021-01-01', '2021-01-10'))
