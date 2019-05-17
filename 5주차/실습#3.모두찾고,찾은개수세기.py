def findAllNCount(filename,key):
    intext = open(filename,"r")
    outtext = open("result.txt","w")
    text = intext.read()
    position = text.find(key)
    count = 0
    if position == -1:
        outtext.write(key + " is not found\n")
    else:
        while position != -1:
            count += 1
            position = text.find(key,position + 1)
        if count == 1:
            outtext.write(key + " is found " + str(count) + " time.\n")
        else:
            outtext.write(key + " is found " + str(count) + " times.\n")
    outtext.close()
    intext.close()
