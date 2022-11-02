StartPtr = -1
EndPtr = 0
QueueFull = 9
Queue = [None for i in range (10)]

def InitQ ():
    global StartPtr, EndPtr , QueueFull, Queue

    StartPtr = -1
    EndPtr = -1
    QueueFull = 9
    for i in range (10):
        Queue[i] = None


def EnQ (Item):
    global StartPtr, QueueFull, Queue
    if StartPtr == QueueFull:
        print ("Queue is full")
    else:
        StartPtr +=1
        Queue[StartPtr] = Item


def DeQ ():
    global EndPtr, StartPtr, Queue
    if EndPtr == StartPtr:
        return -1
    else:
        EndPtr +=1
        Item = Queue[EndPtr]
        Queue[EndPtr] = None
        return Item

def ViewQ ():
    print ("SP Position: ",StartPtr)
    print ("EP Position: ",EndPtr)
    for i in range (10):
        print (i, Queue[i])


def GetOption ():
    print ("1. Enqueue")
    print ("2. Dequeue")
    print ("3.View Queue:")
    print ("4.Initialise Queue")
    print ("5. End Program")
    choice = int(input("Choose a queue operation: "))
    return choice

InitQ()
choice = GetOption()
while choice != 5:
    if choice == 1:
        Item = str(input("Enter a value to add: "))
        EnQ(Item)
    elif choice == 2:
        x = DeQ()
        if x == -1:
            print ("Underflow Occured")
        else:
            print(x, "was dequeued")
    elif choice == 3:
        ViewQ()
    elif choice == 4:
        InitQ()

    choice = GetOption ()



















