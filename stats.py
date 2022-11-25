
def stats():
    try:
        file = open("MyFile.txt", "rt")

        LineCount = 0
        Text = file.readline()
        while Text != "":
            LineCount += 1
            Text = file.readline()
        file.close()

        if LineCount > 0 :
            CharCount = 0
            WordCount = 0
            file = open("MyFile.txt", "rt")
            Text = file.readline()
            while Text != "":
                for i in range (len(Text) - 1):
                    Char = Text [i].upper()
                    if ascii(Char) != ascii(' '):
                        CharCount +=1
                    elif ascii(Char) == ascii(' '):
                        WordCount +=1
                Text = file.readline()
            file.close()
            WordCount = WordCount + LineCount
            print ("no of lines in file:", LineCount)
            print ("no of characters in file:", CharCount)
            print ("no of words in file:",WordCount)
        else:
            print ("File is empty")
    except IOError:
        print ("File not found ")

stats()
