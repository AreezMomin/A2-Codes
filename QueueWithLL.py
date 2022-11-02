class ListNode :
    def __init__ (self):
        Data = ""
        Ptr = 0

HeadPtr = 0
TailPtr = 0
FreePtr = 0
Queue = [ListNode() for i in range (10)]

def InitQ () :
    global Queue, FreePtr, HeadPtr, TailPtr
    HeadPtr = -1
    TailPtr = -1
    FreePtr = 0
    for i in range (10):
        Queue.append (None , i + 1)
    Queue[9].Ptr = -1

def EnQ(Item):
    if FreePtr == -1:
        print ("Overflow Occured")
    else:
        HeadPtr = FreePtr
        Queue[HeadPtr].Data = Item
        FreePtr = Queue[FreePtr].Ptr

def DeQ():
    if HeadPtr == TailPtr:
        print ("Underflow")
        return -1
    else:
        TailPtr +=1
        Item = Queue[TailPtr].Data
        Queue[TailPtr].Data = None
        return Item

def OutputNodes ():
    Thisnodeptr = HeadPtr:







