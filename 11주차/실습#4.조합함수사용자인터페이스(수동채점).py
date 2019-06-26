def combination():
    print("This program computes combination of two natural nubmers, n and r")
    print("Press Control-C to quit.")
    print("Press Enter when you are ready.")
    while True:
        try:
            x = input()
            assert x == ""
            while True:
                cnt = 0
                while True:
                    try:
                        n = int(input("Enter n: \n"))
                        break
                    except KeyboardInterrupt:
                        cnt += 1
                        break
                    except ValueError:
                        print("정수만 입력하세요.")
                        continue
                while True:
                    if cnt != 0:
                        break
                    try:
                        r = int(input("Enter r: \n"))
                        break
                    except KeyboardInterrupt:
                        cnt += 1
                        break
                    except:
                        print("정수만 입력하세요.")
                        continue
                if cnt != 0:
                    break
                ans = combPascal(n, r)
                print(n,"C",r,"=", ans)
        except KeyboardInterrupt:
            print("Goodbye!")
            break
        except:
            print("계속하시려면 Enter, 끝내시려면 Control-C를 입력하세요.")
            continue

def combPascal(n, r):
    vector = [1] * (r + 1)
    for _ in range(1, n - r + 1):
        for j in range(1, r + 1):
            vector[j] = vector[j-1] + vector[j]
    return vector[r]
