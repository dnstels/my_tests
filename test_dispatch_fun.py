from functools import singledispatch
from datetime import date, datetime, time

@singledispatch
def format(label):
    return label

@format.register
def _(label: date):
    return label.strftime("%Y-%m-%d")

@format.register(datetime)
def _(label):
    return label.strftime("%Y-%m-%d %H:%M:%S")

@format.register(time)
def _(label):
    return label.strftime("%H:%M:%S")

print(format("today"))
print(format(date(2021, 7, 28)))
print(format(datetime(2021, 7, 28, 17, 25, 10)))
print(format(time(17, 25, 10)))
