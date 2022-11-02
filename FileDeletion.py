
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

def DeleteRecord():
    DeleteID = int(input("Enter ID to delete record: "))
    StudentFile =  open("Student.txt" , "rt")
    FileList = [" " for Index in range (100)]
    Deleted = False
    Index = 0
    while True:
        try:
            StdID = StudentFile.readline()

            if StdID == "" :
                break
            StdID =int(StdID)

            if StdID != DeleteID:
                StdName = StudentFile.readline()
                StdClass = StudentFile.readline()
                FileList[Index] = str(StdID)
                Index += 1
                FileList[Index] = StdName
                Index += 1
                FileList[Index] = StdClass
                Index += 1

            else:
                Deleted = True


        except:
            pass
    StudentFile.close

    if Deleted:
        StudentFile = open("Student.txt" , "wt")
        Index = 0
        StdID = FileList[Index]
        while StdID != " " :
            Index +=1
            StdName = FileList[Index]
            Index +=1
            StdClass = FileList[Index]
            Index +=1

            StudentFile.write(StdID.strip() + "\n")
            StudentFile.write(StdName.strip() + "\n")
            StudentFile.write(StdClass.strip() + "\n")
            StdID = FileList[Index]
    else:
        print ("ID does not exist")


CreateFile()
DeleteRecord()
















