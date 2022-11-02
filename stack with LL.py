class ListNode :
    def __init__ (self ):
        Data = ""
        Ptr = 0

FreeListPtr = 0
TopPointer = -1
NULL = -1
Stack = [ ListNode() for i in range (10)]

def InitStack ():
    TopPointer = NULL
    FreeListPtr = 0
    for i in range (10):
        Stack[i]. Data = None
        Stack[i]. Ptr = i + 1
    Stack[9].Ptr = -1

def PushItem (Item) :
    global FreeListPtr, Stack, TopPointer
    if FreeListPtr == NULL:
        print ("Overflow occured")
    else:
        NewNodePtr = FreeListPtr
        Stack[NewNodePtr].Data = Item
        FreeListPtr = Stack[FreeListPtr].Ptr
        Stack[NewNodePtr].Ptr = TopPointer
        TopPointer = NewNodePtr

def Pop():
    global TopPointer, Stack
    if TopPointer == NULL:
        return -1
    else:
        Item = Stack[TopPointer]. Data
        Stack[TopPointer]. Data  = None
        ThisNodePtr = TopPointer
        TopPointer = Stack[TopPointer].Ptr
        Stack[ThisNodePtr].Ptr = FreeListPtr
        ThisNodePtr = FreeListPtr
        return Item

def OutputNode() :
    global TopPointer, Stack
    ThisNodePtr = TopPointer
    if TopPointer == NULL:
        print ("Stack Empty")
    else:
        while ThisNodePtr != -1:
            print ( ThisNodePtr, Stack[ThisNodePtr].Data)
            ThisNodePtr = Stack[ThisNodePtr].Ptr


def GetOptions():
    print ("1. Push Item")
    print ("2. Pop Item ")
    print ("3. Output stack node")
    print ("4. Initialise Stack")
    print ("5. Exit Program")
    choice = int(input (" Choose Operation to perform: "))
    return choice

InitStack()
choice = GetOptions()
while choice != 5:
    if choice == 1:
        Item = input ( " Enter value to push: ")
        PushItem(Item)
    elif choice == 2:
        x = Pop()
        if x == -1:
            print ("Stack empty")
        else:
            print (x, "was removed")
    elif choice == 3 :
        OutputNode()
    elif choice == 4:
        InitStack()
    choice = GetOptions()









