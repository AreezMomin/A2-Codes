import os


def AddToSFile():
    added = False
    exists = False
    try:
        StudentFile = open("Student.txt","rt")
    except:
        StudentFile = open("Student.txt","wt")
        ID = int(input("Enter Student ID: "))
        Name = input("Enter Student Name: ")
        Class = input("Enter Student Class: ")
        Fee = float(input("Enter Student Fee: "))

        StudentFile.write(str(ID) +"\n")
        StudentFile.write(Name +"\n")
        StudentFile.write(Class +"\n")
        StudentFile.write(str(Fee)+"\n")

        StudentFile.close

        StudentFile = open("Student.txt","rt")

    StudentT = open("StudentTemp.txt" , "wt")

    ID = int(input("Enter Student ID: "))
    Name = input("Enter Student Name: ")
    Class = input("Enter Student Class: ")
    Fee = float(input("Enter Student Fee: "))


    StdID = StudentFile.readline()
    StdName = StudentFile.readline()
    StdClass = StudentFile.readline()
    StdFee = StudentFile.readline()

    while StdID != "":

        if int(StdID) == ID :
            exists = True
            added = True
            print ("Record already exists")
            break

        elif int(StdID) > ID and not added  :
            added = True
            StudentT.write(str(ID) + '\n')
            StudentT.write(Name + '\n')
            StudentT.write(Class + '\n')
            StudentT.write(str(Fee) + '\n')

        StudentT.write(StdID)
        StudentT.write(StdName)
        StudentT.write(StdClass)
        StudentT.write(StdFee)


        StdID = StudentFile.readline()
        StdName = StudentFile.readline()
        StdClass = StudentFile.readline()
        StdFee = StudentFile.readline()
    if not added :
        StudentT.write(str(ID) + '\n')
        StudentT.write(Name + '\n')
        StudentT.write(Class + '\n')
        StudentT.write(str(Fee) + '\n')



    StudentFile.close()
    StudentT.close()
    if not exists:
        os.remove("Student.txt")
        os.rename("StudentTemp.txt", "Student.txt")
    elif exists:
        os.remove("StudentTemp.txt")




choice = int(input("Enter 1 to input: \nEnter -1 to exit: "))
while choice != -1:
    AddToSFile()
    choice = int(input("Enter 1 to input: \nEnter -1 to exit: "))



