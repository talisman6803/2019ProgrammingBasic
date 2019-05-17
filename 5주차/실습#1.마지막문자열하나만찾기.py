def findLast(filename,key) :
    intext = open(filename, "r", encoding="UTF-8")
    outtext = open("result.txt", "w")
    text = intext.read()
    last_position = text.find(key)
    while True :
        temp = last_position
        last_position = text.find(key,last_position+1)
        if last_position == -1 :
            if temp != -1 :
                outtext.write(key + " is at " + str(temp) + " the last time.\n")
            else :
                outtext.write(key + " is not found.\n")
        else :
            continue
        break
    intext.close()
    outtext.close()
    print("Done")
