def timePassed(fromTime, toTime):
    (hour1,_,minute1) = fromTime.partition(":")
    (hour2,_,minute2) = toTime.partition(":")
    hour = int(hour2) - int(hour1)
    if minute1 > minute2:
        hour = int(hour2) - int(hour1) - 1
        minute = 60 - int(minute1) + int(minute2)
    else:
        hour = int(hour2) - int(hour1)
        minute = int(minute2) - int(minute1)
    return str(hour) + ":" + str(minute)
    
print(timePassed("03:12","03:25")) # "0:13"
print(timePassed("11:45","13:15")) # "1:30"
print(timePassed("06:15","07:45")) # "1:30"
print(timePassed("03:34","05:00")) # "1:26"
