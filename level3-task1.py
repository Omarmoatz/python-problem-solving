# 1 date defference
from datetime import datetime

def date_difference(date1, date2): 
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((date2 - date1).days)

# print(date_difference('2021-01-01', '2021-01-10'))

# Make a temperature/measurement converter. Write a script that can convert
# Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different
# ways

# 1
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0/9.0

def celsius_to_fahrenheit(c):
    return (c * 9.0/5.0) + 32

print(fahrenheit_to_celsius(100))
print(celsius_to_fahrenheit(37.77777777777778))

# 2
def inches_to_centimeters(inches):
    return inches * 2.54

def centimeters_to_inches(centimeters):
    return centimeters / 2.54

print(inches_to_centimeters(10))
print(centimeters_to_inches(25.4))
