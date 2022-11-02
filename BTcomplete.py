class TreeNode :
    def __init__(self):
        self.Data = ""
        self.LP = 0
        self.RP = 0

Nullptr = -1
Freeptr = 0
Rootptr = -1
Tree = [TreeNode () for i in range (11)]

def InitialiseBT ():
    global Freeptr , Tree , Rootptr, Nullptr
    Freeptr = 0
    Nullptr = -1
    Rootptr = -1
    for i in range (11):
        Tree[i].Data = ""
        Tree[i].LP = i + 1
        Tree[i].RP = -1
    Tree [10].LP = -1

def FindNode(SearchItem):
    global Rootptr, Tree
    Thisnodeptr = Rootptr
    while Thisnodeptr != -1 and Tree[Thisnodeptr].Data != SearchItem:
        if Tree [Thisnodeptr].Data > SearchItem:
            Thisnodeptr = Tree[Thisnodeptr]. LP
        else:
            Thisnodeptr = Tree [Thisnodeptr]. RP
    return Thisnodeptr


def InsertNode ( NewItem ):
    global Freeptr, Rootptr , Nullptr, Tree
    TurnedLeft = False
    if Freeptr != Nullptr:
        Newnodeptr = Freeptr
        Tree [Newnodeptr]. Data = NewItem
        Freeptr = Tree[Freeptr].LP
        Tree [Newnodeptr] . LP = -1

        if Rootptr == Nullptr:
            Rootptr = Newnodeptr

        else:
            Thisnodeptr = Rootptr
            while Thisnodeptr != Nullptr:
                Prevnodeptr = Thisnodeptr

                if Tree[Thisnodeptr].Data > NewItem:
                    TurnedLeft = True
                    Thisnodeptr = Tree[Thisnodeptr].LP
                else:
                    TurnedLeft = False
                    Thisnodeptr = Tree[Thisnodeptr].RP


            if TurnedLeft == True:
                Tree[Prevnodeptr].LP = Newnodeptr
            else:
                Tree[Prevnodeptr].RP = Newnodeptr
    else:
        print ("Overflow occured")


def TraverseBT (Rootptr):
    global Tree , Freeptr, Nullptr
    if Rootptr != Nullptr:
        TraverseBT ( Tree [Rootptr].LP)
        print (Tree[Rootptr].Data)
        TraverseBT ( Tree [Rootptr]. RP)


def GetOption ():
    print ("1. Insert Node")
    print ("2. Search Node ")
    print ("3. Traverse Binary Tree ")
    print ("4. Initialise Binary Tree")
    print ("5. Exit Program")
    choice = int(input(" Select one Binary Tree operation: "))
    return choice

#mainprogram

InitialiseBT()
choice = GetOption()

while choice != 5:
    if choice == 1:
        NewItem = input("Enter data value: ")
        InsertNode(NewItem)
        TraverseBT(Rootptr)
    elif choice == 2:
        SearchItem = input("Enter data value to search: ")
        Position = FindNode(SearchItem)
        if Position == -1:
            print ("Value does not exists in BT")
        else:
            print ("Value found at: ", Position)
            for i in range (11):
                print (i, Tree[i].LP, Tree[i].Data, Tree[i].RP)
    elif choice == 3:
        TraverseBT(Rootptr)
    elif choice == 4:
        InitialiseBT()

    choice = GetOption()








































