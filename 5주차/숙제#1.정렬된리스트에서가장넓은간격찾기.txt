import random
def testSearchWidestGap():
    db = random.sample(range(500),100)
    print("Searching the widest gap...")
    db.sort()
    print(db)
    index, gap = searchWidestGap(db)
    print("The widest gap is:", gap)
    print("between", db[index], "and", db[index+1])
    print("at", index)
def searchWidestGap(db):
    if len(db) != 0:
        count = 1
        dis = 0
        pos = 0
        while count != len(db):
            if db[count] - db[count - 1] > dis:
                dis = db[count] - db[count - 1]
                pos = count -1
            count += 1
        return (dis,pos)
    else:
        return (0,-1)

testSearchWidestGap()
