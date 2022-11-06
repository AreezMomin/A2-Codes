def CreateFile():
    StudentFile = open("Student.txt", "wt")
    StdName = input("Enter Student Name: ")
    while StdName != "" :
        StdAge  = int(input("Enter Student Age: "))
        StdClass = input("Enter Student Class and Section: ")

        StudentFile.write( StdName + '#' + str(StdAge) + '#' + StdClass + "\n")

        StdName = input("Enter Student Name \n Press ENTER to Exit: ")

    StudentFile.close()


def ShowFile ():
    StudentFile = open("Student.txt" , "rt")
    TextLine = StudentFile.readline()
    while TextLine != "":
        StdName = ""
        StdAge = ""
        StdClass = ""
        field = 0
        for i in range (len(TextLine) - 1):
            Thischar = TextLine[i]
            if Thischar == '#':
                field +=1
            elif field == 0:
                StdName += TextLine[i]
            elif field == 1:
                StdAge += TextLine[i]
            else :
                StdClass += TextLine[i]

        print(StdName , StdAge , StdClass )
        TextLine = StudentFile.readline()

    StudentFile.close()

def SearchFile ():
    StudentFile = open("Student.txt" , "rt")
    SearchName = input("Enter the student name to search for: ")
    TextLine = StudentFile.readline()
    found = False
    while TextLine != "":
        field = 0
        StdName = ""
        StdAge = ""
        StdClass = ""
        for i in range (len(TextLine) -1):
            Thischar = TextLine[i]
            if Thischar == '#':
                field +=1
            elif field == 0:
                StdName += Thischar
            elif field == 1:
                StdAge += Thischar
            else:
                StdClass += Thischar

        if StdName == SearchName:
            found = True
            print (StdName , StdAge , StdClass)


        TextLine = StudentFile.readline()
    if not found: print(SearchName,"not found")

    StudentFile.close()

def DeleteFromFile():
    StudentFile = open("Student.txt", "rt")
    DeleteName = input("Enter the student name to delete: ")
    RecordList = []
    TextLine = StudentFile.readline()
    deleted = False
    while TextLine != "":
        field = 0
        StdName = ""
        StdAge = ""
        StdClass = ""
        for i in range (len(TextLine)-1):
            Thischar = TextLine[i]
            if Thischar == '#':
                field += 1
            elif field == 0:
                StdName += Thischar
            elif field == 1:
                StdAge += Thischar
            else:
                StdClass += Thischar

        if DeleteName != StdName :
            RecordList.append(TextLine)
        else:
            deleted = True
        TextLine = StudentFile.readline()
    StudentFile.close()
    StudentFile = open("Student.txt", "wt")

    for i in range (len(RecordList)):
        TextLine = RecordList[i]
        StudentFile.write(TextLine)


    StudentFile.close()
    if not deleted:
        print("Entered record name doesn't exists")
    ShowFile()

def EditInFile():
    StudentFile = open("Student.txt", "rt")
    EditName = input("Enter the student name to edit: ")
    RecordList = []
    TextLine = StudentFile.readline()
    edited = False
    while TextLine != "":
        field = 0
        StdName = ""
        StdAge = ""
        StdClass = ""
        for i in range (len(TextLine)-1):
            Thischar = TextLine[i]
            if Thischar == '#':
                field += 1
            elif field == 0:
                StdName += Thischar
            elif field == 1:
                StdAge += Thischar
            else:
                StdClass += Thischar

        if EditName != StdName :
            RecordList.append(TextLine)
        else:
            edited = True
            StdName = input("Enter new student name: ")
            StdAge = int(input("Enter new student age: "))
            StdClass = input("Enter new student class: ")
            TextLine = (StdName + '#' + str(StdAge) + '#' + StdClass + "\n")
            RecordList.append(TextLine)

        TextLine = StudentFile.readline()
    StudentFile.close()
    StudentFile = open("Student.txt", "wt")

    for i in range (len(RecordList)):
        TextLine = RecordList[i]
        StudentFile.write(TextLine)


    StudentFile.close()
    if not edited:
        print("Entered record name doesn't exists")
    ShowFile()


Option = int(input("1.CreateFile \n2.SearchFile \n3.Delete Record \n4.Edit a record \n5.Display File \n6.Exit Program: \n"))

while Option != 6:
    if Option == 1:
        CreateFile()
    elif Option == 2:
        SearchFile()
    elif Option == 3:
        DeleteFromFile()
    elif Option == 4:
        EditInFile()
    elif Option == 5:
        ShowFile()

    Option = int(input("1.CreateFile \n2.SearchFile \n3.Delete Record \n4.Edit a record \n5.Display File \n6.Exit Program: \n"))
























