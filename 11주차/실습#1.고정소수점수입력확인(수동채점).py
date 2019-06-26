def input_float():
    while True :
        try :
            x = input("고정소수점을 입력하세요:")
            x = int(x)
            print("정수를 입력하셨어요.")
        except ValueError :
            try:
                y = float(x)
                return x
            except ValueError:
                print("잘못 입력하셨어요.")
                continue
        
