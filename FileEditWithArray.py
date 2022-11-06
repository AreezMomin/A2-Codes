def CreateFile():
    StudentFile = open("Student.txt", "wt")
    StdID = int(input("Enter Student ID: "))
    while StdID != -1:
        StdName = input("Enter Student Name: ")
        StdClass = input("Enter Student Class and Section: ")

        StudentFile.write(str(StdID) + "\n")
        StudentFile.write(StdName + "\n")
        StudentFile.write(StdClass + "\n")

        StdID = int(input("Enter Student ID: \n Input -1 to Exit: "))

    StudentFile.close()

def EditRecord():
    EditID = int(input("Enter ID to delete record: "))
    StudentFile =  open("Student.txt" , "rt")
    FileList = [ "" for i in range (0)]
    Index = 0
    edited = False
    while True:
        try:
            StdID = StudentFile.readline()

            if StdID == "" :
                break
            StdID =int(StdID)

            StdName = StudentFile.readline()
            StdClass = StudentFile.readline()

            if StdID == EditID :
                edited = True
                StdID = input("Enter new ID: ")
                StdName = input("Enter new Name: ")
                StdClass = input("Enter new Class: ")

                FileList.append(str(StdID))
                FileList.append(StdName)
                FileList.append(StdClass)
            else:
                FileList.append(str(StdID))
                FileList.append(StdName)
                FileList.append(StdClass)

        except:
            pass
    StudentFile.close
    if edited :
        StudentFile = open("Student.txt", "wt")
        Index = 0
        length = len (FileList) -1


        while Index <= length:
            StdID = FileList[Index]
            Index +=1
            StdName = FileList[Index]
            Index +=1
            StdClass = FileList[Index]
            Index +=1
            StudentFile.write(StdID.strip() + "\n")
            StudentFile.write(StdName.strip()+"\n")
            StudentFile.write(StdClass.strip()+"\n")

        StudentFile.close

CreateFile()
EditRecord()
























