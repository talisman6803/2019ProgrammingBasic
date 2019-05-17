import random
def testBinSearchClosest():
    db = random.sample(range(500),100)
    print("Binary search closest function test")
    db.sort()
    print(db)
    for _ in range(10):
        key = random.randrange(500)
        index = binSearchClosest(db,key)
        print("The closest value to", key, ":", db[index], "at index", index)
def binSearchClosest(db,key):
    if len(db) == 0:
        return None
    else:
        pos = 0
        temp = abs(db[0] - key)
        for i in range(len(db)):
            if abs(db[i] - key) < temp:
                temp = abs(db[i] - key)
                pos = i
            if abs(db[i] - key) > temp and i > pos:
                break
        return pos

testBinSearchClosest()
