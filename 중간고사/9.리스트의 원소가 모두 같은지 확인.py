def allequal(ns):
    if len(ns) > 1:
        if ns[0] == ns[1]:
            return True and allequal(ns[1:])
        else:
            return False
    else:
        return True

print(allequal([4, 6, 5, 3, 7, 6, 2, 1, 3, 2])) # False
print(allequal([5, 5, 4, 4, 6, 5, 1, 2, 2, 2])) # False
print(allequal([3, 2, 2, 2, 2, 2, 2, 2, 2, 2])) # False
print(allequal([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) # True
print(allequal([2])) # True
print(allequal([])) # True
