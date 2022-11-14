import os

def AddInFile():
    ID = int(input("Enter Student ID: \nEnter -1 to exit: "))
    while ID != -1:
        Name = input("Enter Student Name: ")
        Class = input("Enter Student Class: ")
        added = False
        try:
            StudentFile = open("Student.txt", "rt")
        except:
            StudentFile = open("Student.txt", "xt")
            StudentFile = open("Student.txt", "rt")
        StudentTemp = open("StudentTempFile.txt","wt")

        StdID = StudentFile.readline()
        while StdID != "":
            StdID = int(StdID)
            StdName = StudentFile.readline()
            StdClass = StudentFile.readline()

            if StdID == ID :
                added = True
                print("Student ID already exists")

            elif not added and StdID > ID :
                added = True
                StudentTemp.write(str(ID) + '\n')
                StudentTemp.write(Name + '\n')
                StudentTemp.write(Class + '\n')

            StudentTemp.write(str(StdID) + '\n')
            StudentTemp.write(StdName )
            StudentTemp.write(StdClass )

            StdID = StudentFile.readline()
        if not added:
            StudentTemp.write(str(ID) + '\n')
            StudentTemp.write(Name + '\n')
            StudentTemp.write(Class + '\n')

        StudentFile.close()
        StudentTemp.close()

        os.remove("Student.txt")
        os.rename("StudentTempFile.txt", "Student.txt")

        ID = int(input("Enter Student ID: \nEnter -1 to exit: "))


def DeleteFromFile():
    DeleteID = int(input("Enter the Student ID to delete: "))
    StudentFile = open("Student.txt" , "rt")
    StudentTemp = open("StudentTempFile.txt", "wt")
    deleted = False
    StdID = StudentFile.readline()

    while StdID != "":
        StdID = int(StdID)
        StdName = StudentFile.readline()
        StdClass = StudentFile.readline()

        if StdID != DeleteID :
            StudentTemp.write( str(StdID) + '\n')
            StudentTemp.write( StdName )
            StudentTemp.write( StdClass )

        else:
            deleted = True

        StdID = StudentFile.readline()

    if not deleted :
        print("Student ID doesn't exists")

    StudentFile.close()
    StudentTemp.close()

    os.remove("Student.txt")
    os.rename("StudentTempFile.txt", "Student.txt")















