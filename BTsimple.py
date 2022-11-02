class  TreeNode :
    def __init__ (self):
        self. Data = ""
        self. LP = 0
        self. RP = 0

Freenodeptr = 0
Nullptr = -1
Rootptr = -1
Tree = [TreeNode () for i in range (11)]
isadded = False

def InitBT ():
    global Tree, Nullptr, Rootptr, Freenodeptr
    Freenodeptr = 0
    Rootptr = -1
    Nullptr = -1
    for i in range (11):
        Tree[i].LP = -1
        Tree[i].Data = ""
        Tree[i].RP = -1


def InsertNode(NewItem):
    global Tree, Nullptr, Rootptr, Freenodeptr
    Thisnodeptr = 0
    isadded = False
    if Freenodeptr != 10:
        if Tree[Thisnodeptr].Data == "":
            Tree[Thisnodeptr].Data = NewItem
            Rootptr = Thisnodeptr
        else:
            Tree[Freenodeptr].Data = NewItem
            while isadded == False :
                if Tree[Thisnodeptr]. Data  > NewItem:
                    if Tree[Thisnodeptr].LP == -1:
                        Tree[Thisnodeptr].LP = Freenodeptr
                        isadded = True
                    else:
                        Thisnodeptr = Tree[Thisnodeptr].LP
                if Tree[Thisnodeptr]. Data < NewItem:
                    if Tree[Thisnodeptr].RP == -1:
                        Tree[Thisnodeptr].RP = Freenodeptr
                        isadded = True
                    else:
                        Thisnodeptr = Tree[Thisnodeptr].RP
        Freenodeptr = Freenodeptr +  1
    else:
        print ("Overflow occured")


def OutputBT ():
    global Tree, Rootptr, Freenodeptr
    print ("Root Pointer: ", Rootptr)
    print ("Free node Pointer: ", Freenodeptr)
    for i in range (11):
        print (i, Tree[i].LP, Tree[i].Data , Tree[i].RP)


def Getoption():
    print ("1. Initialise Binary Tree")
    print ("2. Insert Node ")
    print ("3. View Binary Tree")
    print ("4. Exit Program ")
    choice = int(input("Choose a Binary Tree operation: "))
    return choice

InitBT()
choice = Getoption()
while choice != 4:
    if choice == 1:
        InitBT()
    elif choice == 2:
        NewItem = input("Enter the value to insert: ")
        InsertNode(NewItem)
    elif choice == 3:
        OutputBT()

    choice = Getoption()


































