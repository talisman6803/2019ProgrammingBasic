def factorial():
    while True:
        try:
            n = int(input("자연수를 입력해주세요: "))
            assert n >= 0
            print("factorial(",n,") = ",fac(n),sep='')
        except ValueError as e:
            print(e, "은(는) 자연수가 아닙니다.")
        except AssertionError:
            print(n,"은(는) 자연수가 아닙니다.")
        else:
            print("또 오세요!")
            break

def fac(n):
    
    ans = 1
    while n > 0:
        ans = n * ans
        n = n - 1
    return ans
