class Listnode:
    def __init__ (self):
        self.Data = ""
        self.Ptr = 0

freelistpointer = 0
nullpointer = -1
newnodepointer = -1
startpointer = -1
Llist = [Listnode () for i in range(9)]



def initialiseList ():
    global freelistpointer, newnodepointer,nullpointer,startpointer
    freelistpointer = 0
    newnodepointer = nullpointer
    startpointer = -1
    for i in range (9):
        Llist[i].Ptr = i + 1
    Llist[8].Ptr = nullpointer


def insertnode (NewItem):
    global freelistpointer, startpointer,nullpointer
    if freelistpointer != nullpointer:
        newnodepointer = freelistpointer
        Llist[newnodepointer].Data = NewItem
        freelistpointer = Llist[freelistpointer].Ptr

        thisnodepointer = startpointer
        prevnodepointer = -1
        while thisnodepointer != nullpointer and Llist[thisnodepointer].Data < NewItem:
            prevnodepointer = thisnodepointer
            thisnodepointer = Llist[thisnodepointer].Ptr

        if thisnodepointer == startpointer:
            Llist[newnodepointer].Ptr = startpointer
            startpointer = newnodepointer

        else:
            Llist[newnodepointer].Ptr = Llist[prevnodepointer].Ptr
            Llist[prevnodepointer].Ptr = newnodepointer




def deletenode (DeleteItem):
    global startpointer, nullpointer, freelistpointer
    thisnodepointer = startpointer
    while thisnodepointer != nullpointer and Llist[thisnodepointer].Data != DeleteItem:
        prevnodepointer = thisnodepointer
        thisnodepointer = Llist[thisnodepointer].Ptr

    if thisnodepointer != nullpointer:
        if thisnodepointer == startpointer:
            startpointer = Llist[thisnodepointer].Ptr
        else:
            Llist[prevnodepointer].Ptr = Llist[thisnodepointer].Ptr
        Llist[thisnodepointer].Ptr = freelistpointer
        freelistpointer = thisnodepointer



def viewlist ():
    global freelistpointer, startpointer
    print ("Freelist pointer= ",freelistpointer)
    print ("Startpointer = ",startpointer)

    for index in range (9):
        print (index , Llist[index].Data,Llist[index].Ptr)


def getoption ():
    print ("LinkList options: ")
    print ("1. View LinkList")
    print ("2. InsertNode")
    print ("3. DeleteNode")
    print ("4. Initialise List")
    print ("5. Exit program")
    choice = int(input("Please select a option: "))

    return choice

initialiseList()
choice = getoption()
while choice != 5:
    if choice == 1:
        viewlist()
    elif choice == 2:
        NewItem = input("Please enter value to insert: ")
        insertnode(NewItem)
    elif choice == 3:
        DeleteItem = input("Please enter value to delete: ")
        deletenode(DeleteItem)
    elif choice == 4:
        initialiseList()

    choice = getoption()












