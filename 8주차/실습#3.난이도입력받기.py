def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if (level == "상"):
        return 10
    elif (level == "중"):
        return 8
    else:
        return 6
