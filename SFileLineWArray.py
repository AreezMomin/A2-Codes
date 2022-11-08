
def AddToFile():
    added = False
    try:
        StudentFile =open("StudentFileSeqLine.txt", "rt")
    except:
        StudentFile =open("StudentFileSeqLine.txt", "wt")
        StdID = int(input("Enter Student ID: "))
        StdName = input("Enter Student Name: ")
        StdClass = input("Enter Student Class: ")
        StdFees = float(input("Enter Student fees: "))
        StudentFile.write ( str(StdID) +'#'+ StdName +'#'+  StdClass +'#'+  str(StdFees) + '\n')
        StudentFile.close()
        StudentFile = open("StudentFileSeqLine.txt", "rt")

    StRecord = []


    ID = int(input("Enter new  Student ID: "))
    Name = input("Enter new Student Name: ")
    Class = input("Enter new Student Class: ")
    Fees = float(input("Enter new Student fees: "))
    TextLine = str(ID) +'#'+ Name +'#'+ Class +'#'+  str(Fees) + '\n'
    RecLine = StudentFile.readline()
    while RecLine != "":
        i = 0
        ThisChar = RecLine[i]
        StdID = ""
        while ThisChar != '#':
            StdID += ThisChar
            i +=1
            ThisChar = RecLine[i]

        StdID = int(StdID)

        if StdID > ID and not added  :
            added = True
            StRecord.append(TextLine)

        StRecord.append(RecLine)
        RecLine = StudentFile.readline()


    if not added:
        StRecord.append(TextLine)

    StudentFile.close()

    StudentFile = open("StudentFileSeqLine.txt", "wt")

    for i in range (len(StRecord)):
        TextLine = StRecord[i]
        StudentFile.write(TextLine)

    StudentFile.close()


Choice = int(input("Enter 1 to add: \n Enter -1 to exit: "))
while Choice != -1:
    AddToFile()
    Choice = int(input("Enter 1 to add: "))



































