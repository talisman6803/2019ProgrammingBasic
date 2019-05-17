# 제출시 파일 이름 형식은 2019000000-도선생.py 

# 반 : 10시
# 학번 : 2019067565
# 이름 : 전상민
# 구글클래스 이름 : Étoile Jeon 혹은 Sam RENAULT

## 2. 2차방정식 근의 공식

import math
def quadraticEquationPositive(a,b,c):
    if a != 0:
        pb = (b**2)-(4*a*c)
        if pb <= 0:
	return None
        else:
            ans1 = (-1 * b + ((b**2)-(4*a*c))**(0.5))/2/a
            ans2 = (-1 * b - ((b**2)-(4*a*c))**(0.5))/2/a
            return (ans1, ans2)
    else:
        return None

### 3. 24시간 시계 형식 확인

def validClock24(time):
    (hour, colon, minute) = time.partition(":")
    return (("00" <= hour <= "23" and "00" <= minute <= "59") or (hour == "24" and minute == "00")) and (len(hour) == 2 and len(minute) == 2)

### 4. 24시간 시계를 12시간 시계로 변환

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

### 5. 소요시간 계산하기

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

### 6. 일반재귀 함수를 꼬리재귀 함수로 변환하기 
def adjust(ns):
    if len(ns) > 1:
        if ns[0] < ns[1]:
            return [ns[0]+1] + adjust(ns[1:])
        elif ns[0] > ns[1]:
            return [ns[0]-1] + adjust(ns[1:])
        else:
            return [ns[0]] + adjust(ns[1:])
    else:
        return ns

def adjustT(ns):
    def loop(ns,rs):
        if len(ns) > 1:
            if ns[0] < ns [1]:
                rs += [ns[0]+1]
                return loop(ns[1:],rs)
            elif ns[0] > ns[1]:
                rs += [ns[0]-1]
                return loop(ns[1:],rs)
            else:
                rs += [ns[0]]
                return loop(ns[1:],rs)
        else:
            return rs + ns
    return loop(ns,[])

### 7. 꼬리재귀 함수를 while 루프 함수로 변환하기

def adjustW(ns):
    rs = []
    while len(ns) > 1:
        if ns[0] < ns[1]:
            rs += [ns[0]+1]
        elif ns[0] > ns[1]:
            rs += [ns[0]-1]
        else:
            rs += [ns[0]]
        ns = ns[1:]
    return rs + ns

### 8. for 루프 함수로 만들기
def adjustF(ns):
    rs = []
    for i in range(len(ns)-1):
        if ns[i] < ns[i+1]:
            rs += [ns[i]+1]
        elif ns[i] > ns[i+1]:
            rs += [ns[i]-1]
        else:
            rs += [ns[i]]
    return rs

### 9. 리스트의 원소가 모두 같은지 확인

def allequal(ns):
    if len(ns) > 1:
        if ns[0] == ns[1]:
            return True and allequal(ns[1:])
        else:
            return False
    else:
        return True

### 10. 동일화 노력

def equalizer(ns):
    count = 0
    if len(ns) > 1:
        while allequal(ns) != True:
            ns = adjust(ns)
            count += 1
    return count

### 11. 아나그램 확인 (sort() 함수 사용 금지)

def isanagram(word1,word2):
    while word1 != '':
        if word1[0] in word2:
            pass # 이 부분을 코드로 채운다.
        else:
            return False
    return word2 == ''

### 12. 이진수 덧셈 - 자리수는 같다고 가정

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
