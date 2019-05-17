def findAll(filename,key):
    intext = open(filename,"r")
    outtext = open("result.txt","w")
    text = intext.read()
    position = text.find(key)
    if position == -1:
        outtext.write(key + " is not found.\n")
    else :
        while position != -1:
            outtext.write(key + " is at " + str(position) + ".\n")
            position = text.find(key,position + 1)
    outtext.close()
    intext.close()
