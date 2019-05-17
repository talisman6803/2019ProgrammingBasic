def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)
def front_ok(f):
    if f.isdigit() == False:
        return False

    a,b,c = int(f[0:2]),int(f[2:4]),int(f[4:6])

    if not (0<b<13):
        return False

    if a%4 != 0:
        if b == 2:
            return 0<c<29
        elif b == 4 or b == 6 or b == 9 or b == 11:
            return 0<c<31
        else:
            return 0<c<32

    if a%4 == 0:
        if b == 2:
            return 0<c<30
        elif b == 4 or b == 6 or b == 9 or b == 11:
            return 0<c<31
        else:
            return 0<c<32
def back_ok(s):
    si = s[0:6] + s[7:]
    i,m = 0,0
    while not i == 12:
        m += (i%8+2) * int(si[i])
        i += 1

    print(m)
    m = (11 - m%11)%10
    print(m)
    if int(si[12]) == m:
        return True

    return False
