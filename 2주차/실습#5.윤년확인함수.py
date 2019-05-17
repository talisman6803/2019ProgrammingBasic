def isleapyear(year):
    if year >= 0 :
        if year%4==0: 
            if year%100==0:
                if year%400==0: return True
                else : return False
            else : return True
        else : return False
    else : return None
print(isleapyear(0))
print(isleapyear(1))
print(isleapyear(4))
print(isleapyear(2010))
print(isleapyear(2011))
print(isleapyear(2012))
print(isleapyear(2013))
print(isleapyear(2016))
print(isleapyear(1900))
print(isleapyear(2000))
print(isleapyear(2100))
print(isleapyear(2200))
print(isleapyear(2400))
print(isleapyear(-2000))
