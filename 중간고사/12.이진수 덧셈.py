def addBinary(n1,n2):
    over = 0
    answer = ''
    count = 0
    for d in range(-1,-len(n1)-1,-1):
        total = int(n1[d]) + int(n2[d]) + over
        if total == 1:
            over = 0
            answer = '1' + answer
        elif total == 2:
            over = 1
            answer = '0' + answer
        elif total == 3:
            over = 1
            answer = '1' + answer
        else: # total = 0
            over = 0
            answer = '0' + answer
        count += 1
    if over == 1:
        answer = '1' + answer
    return str(answer)

print(addBinary('','')) # ''
print(addBinary('0','0')) # '0'
print(addBinary('1','0')) # '1'
print(addBinary('0','1')) # '1'
print(addBinary('1','1')) # '10'
print(addBinary('10','11')) # '101'
print(addBinary('11','11')) # '110'
print(addBinary('1011','1101')) # '11000'
print(addBinary('1111','1111')) # '11110'
print(addBinary('11011001','00011011')) # '11110100'
