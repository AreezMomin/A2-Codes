topPointer = -1
basePointer = 0
stack = [None for i in range (0,10)]
Stackfull = 9




def PushItem ():
    global topPointer, Stackfull, stack
    if topPointer == Stackfull:
        print ("Overflow occured cannot push item")
    else:
        item = str(input ("Enter new value to push: "))
        topPointer +=1
        stack[topPointer] = item

def PopItem ():
    global topPointer, basepointer, stack
    if topPointer < basePointer:
        return -1
    else:
        Item = stack[topPointer]
        stack[topPointer] = None
        topPointer -= 1

    return Item

def viewStack():
    print ("Top of Stack Pointer: ", topPointer)
    for i in range (10):
        print ( i , stack[i] )

def GetOption ():
    print ("1. Push Item ")
    print ("2. Pop Item")
    print ("3.View Stack")
    print ("4. Exit Program")
    choice = int(input("Choose a stack operation: "))
    return choice
choice = GetOption()
while choice != 4:
    if choice == 1:
        PushItem()
    elif choice == 2:
        x = PopItem()
        print (x , "was removed")
    elif choice == 3:
        viewStack()
    choice = GetOption()






