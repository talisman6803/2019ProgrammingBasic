def equalizer(ns):
    count = 0
    if len(ns) > 1:
        while allequal(ns) != True:
            ns = adjust(ns)
            count += 1
    return count

def adjust(ns):
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

def allequal(ns):
    if len(ns) > 1:
        if ns[0] == ns[1]:
            return True and allequal(ns[1:])
        else:
            return False
    else:
        return True
    
print(equalizer([4, 6, 5, 3, 7, 6, 2, 1, 3, 2])) # 9
print(equalizer([8, 2, 5, 7, 1, 1, 6, 7, 4, 8])) # 12
print(equalizer([8, 4, 5, 6, 9, 8, 6, 2, 0, 6])) # 14   
print(equalizer([4, 0, 1, 0, 3, 4, 3, 3, 7, 9])) # 13
print(equalizer([1, 6, 5, 6, 8, 5, 3, 3, 3, 8])) # 13
print(equalizer([])) # 0
print(equalizer([5])) # 0
print(equalizer([4, 4, 4])) # 0
print(equalizer([4, 3])) # 1
print(equalizer([4, 5])) # 1
print(equalizer([4, 5, 4])) # 2
print(equalizer([14, 69, 87, 13, 0, 16, 83, 19, 45, 88])) # 92
