import datetime

def telltime():
    today=datetime.datetime.today()
    time=print(f"It is currently {today.strftime("%I")}:{today.strftime("%M")} {today.strftime("%p")},sir")
    return time

def telldate():
    today=datetime.datetime.today()
    date=print(f"The date is {today.strftime("%d")}th {today.strftime("%B")}, {today.strftime("%A")},sir")
    return date
