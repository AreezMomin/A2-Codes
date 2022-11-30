import os
import struct


class StuRec :
    def __init__ (self):
        self.StuID = 0
        self.StuName = "" # 20 characters
        self.StuClass = "" # 4 characters

myRec = StuRec()
recFormat = "i20s4s"
recSize = struct.calcsize(recFormat)

def AddInRandomFile ():
    totalRec = 0
    global myRec, recFormat, recSize
    File = open ("StudentRandom.DAT" , "a+b")
    File.seek(0, os.SEEK_END) # the file handle goes to the EOF
    totalRec = File.tell()/ recSize

    myRec.StuID = int(totalRec) + 1
    print ("Student ID:", myRec.StuID)
    myRec.StuName = input("Enter name: ")
    myRec.StuClass = input("Enter class: ")

    PackData = struct.pack ( recFormat, myRec.StuID, \
            bytes(myRec.StuName , 'ascii'), \
            bytes(myRec.StuClass, 'ascii'))

    File.seek(int(totalRec * recSize ))
    File.write (PackData)
    File.close()
    print()
    print ("Record Added")
    print()
    ReadRandomFile()


def ReadRandomFile():
    global myRec, recFormat, recSize
    totalRec = 0
    PackData = ""
    File = open ("StudentRandom.DAT" , "rb")
    File.seek(0, os.SEEK_END)
    totalRec = File.tell()/ recSize

    for i in range (int(totalRec)):
        File.seek(int(i * recSize)) # file handle goes to the particular record
        PackData = File.read(recSize)
        #unpack data
        myRec.StuID , myRec.StuName , myRec.StuClass = struct.unpack (recFormat , PackData)

        print ("Student ID:", myRec.StuID)
        print ("Student Name:", myRec.StuName.decode())
        print ("Student Class", myRec.StuClass.decode())
        print ()
    File.close()

def DeleteFromRandomFile():
    global myRec, recFormat, recSize
    Deleted = False

    totalRec = 0
    File = open ("StudentRandom.DAT", "rb")
    tempFile = open ("StudentRandomTemp.DAT", "a+b")

    File.seek(0, os.SEEK_END)
    totalRec = File.tell() / recSize

    ReadRandomFile()
    DeleteID = int(input("Enter the Student ID to delete: "))

    if DeleteID <= int(totalRec) :
        for i in range (int(totalRec)):
            File.seek (int( i * recSize))
            PackData = File.read(recSize)
            myRec.StuID , myRec.StuName , myRec.StuClass = struct.unpack (recFormat , PackData)

            if DeleteID != int(myRec.StuID) and not Deleted :
                tempFile.write (PackData)
            else:
                Deleted = True

            if DeleteID != int(myRec.StuID) and Deleted :
                myRec.StuID = int(myRec.StuID) - 1
                PackData = struct.pack ( recFormat, myRec.StuID, myRec.StuName, myRec.StuClass)
                tempFile.write (PackData)


        File.close()
        tempFile.close()
        os.remove ("StudentRandom.DAT")
        os.rename ("StudentRandomTemp.DAT" , "StudentRandom.DAT")

    if Deleted :
        print()
        print ("Record deleted successfully")
        ReadRandomFile()
    else:
        print()
        print (" Record not found")


def EditRandomFile ():
    global myRec, recFormat, recSize
    Edited = False

    totalRec = 0
    File = open ("StudentRandom.DAT", "rb")
    tempFile = open ("StudentRandomTemp.DAT", "a+b")

    File.seek(0, os.SEEK_END)
    totalRec = File.tell() / recSize
    ReadRandomFile()

    EditID = int(input("Enter the Student ID to edit: "))
    if EditID <= int(totalRec) :
        for i in range (int(totalRec)):
            File.seek (int( i * recSize))
            PackData = File.read(recSize)
            myRec.StuID , myRec.StuName , myRec.StuClass = struct.unpack (recFormat , PackData)

            if EditID != int(myRec.StuID):
                tempFile.write (PackData)
            else:
                Edited = True

                myRec.StuName = input("Enter new name: ")
                myRec.StuClass = input("Enter new class: ")
                PackData = struct.pack ( recFormat, myRec.StuID, \
                            bytes(myRec.StuName , 'ascii'), \
                            bytes(myRec.StuClass, 'ascii'))
                tempFile.write(PackData)
        File.close()
        tempFile.close()
        os.remove ("StudentRandom.DAT")
        os.rename ("StudentRandomTemp.DAT" , "StudentRandom.DAT")
    if Edited:
        print()
        print ("Record was successfully edited")
        ReadRandomFile()
    else:
        print()
        print("Record not found")

def SearchInRandomFile():
    global myRec , recFormat , recSize
    Found = False
    totalRec = 0
    File = open ("StudentRandom.DAT" , "rb")
    File.seek(0, os.SEEK_END)
    totalRec = File.tell() / recSize

    SearchID = int(input("Enter ID to search for: "))
    if SearchID <= int(totalRec):
        Found = True

    if Found :
        print ("Student Found")
    else:
        print ("Student not in records")


choice = int(input("1.Add new record to file\n2.Delete record from file\n3.Edit record in file\n4.View File\n5.Exit Program\n"))
while choice != 5:
    if choice == 1:
        AddInRandomFile()
    elif choice == 2:
        DeleteFromRandomFile()
    elif choice == 3:
        EditRandomFile()
    elif choice == 4:
        ReadRandomFile()
    choice = int(input("1.Add new record to file\n2.Delete record from file\n3.Edit record in file\n4.View File\n5.Exit Program\n"))









