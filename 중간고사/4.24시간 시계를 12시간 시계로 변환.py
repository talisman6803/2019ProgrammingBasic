def clock24to12(time):
    (hour, colon, minute) = time.partition(":")
    if hour == "00" or (hour == "24" and minute == "00"):
        return ("12" + ":" + minute + "am")
    elif "01" <= hour <= "11":
        return (str(int(hour)) + ":" + minute + "am")
    elif hour == "12":
        return ("12:" + minute + "pm")
    else:
        return (str(int(hour)-12) + ":" + minute + "pm")

print(clock24to12("00:00")) # "12:00am"
print(clock24to12("00:05")) # "12:05am"
print(clock24to12("09:58")) # "9:58am"
print(clock24to12("11:43")) # "11:43am"
print(clock24to12("12:08")) # "12:08pm"
print(clock24to12("15:50")) # "3:50pm"
print(clock24to12("20:20")) # "8:20pm"
print(clock24to12("24:00")) # "12:00am"
