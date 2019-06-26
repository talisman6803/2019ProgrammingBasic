def input_float_one():
    while True :
        try :
            x = input("고정소수점을 입력하세요:")
            x = int(x)
            print("정수를 입력하셨어요.")
        except ValueError :
            try:
                y = float(x)
                if -1 <= y and 1 >= y: return x
                else: raise overrange
            except overrange:
                print("-1.0 이상 1.0이하의 실수만 입력해주세요.")
                continue
            except:
                print("잘못 입력하셨어요.")
                continue

class overrange(Exception):pass
