def compare(a,b):

    if a == -1:

        if b == -1:

            return -2

        else:

            return b

    else:

        if b == -1:

            return a

        else:

            if a > b:

                return b

            else:

                return a

            

def oneSentencePerLine(filename) :


    intext = open(filename,"r")

    outtext = open("result.txt","w")

    text = intext.read()

    while not text.find("\n") == -1:

        text = text[:text.find("\n")] + text[text.find("\n")+1:]

    cnt = 0

    while True:

        chk1 = text.find(".")

        chk2 = text.find("?")

        chk = compare(chk1, chk2)

        if chk == -2:

            break

        if text[0] == ' ':

            outtext.write(text[1:chk+1]+"\n\n")

        else:

            outtext.write(text[:chk+1]+"\n\n")

        text = text[chk+1:]

        cnt += 1

    outtext.write("There are " + str(cnt) + " sentences in total.\n")

    outtext.close()

    intext.close()

    print("Done")
