def validClock24(time):
    (hour, colon, minute) = time.partition(":")
    return (("00" <= hour <= "23" and "00" <= minute <= "59") or (hour == "24" and minute == "00")) and (len(hour) == 2 and len(minute) == 2)

print(validClock24("00:00")) # True
print(validClock24("00:30")) # True
print(validClock24("09:58")) # True
print(validClock24("12:15")) # True
print(validClock24("23:59")) # True
print(validClock24("24:00")) # True
print(validClock24("7:07")) # False
print(validClock24("07:121")) # False
print(validClock24("13:4")) # False
print(validClock24("00:60")) # False
print(validClock24("24:01")) # False
print(validClock24("25:10")) # False
