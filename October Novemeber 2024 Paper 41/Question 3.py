LinkedList = []
FirstNode = -1
FirstEmpty = 0
for count in range(19):
    LinkedList.append([-1,count+1])
LinkedList.append([-1,-1])

def InsertData():
    global LinkedList
    global FirstNode
    global FirstEmpty
    for count in range(5):
        if FirstEmpty !=-1: #FirstEmpty(2)
            nextEmpty = LinkedList[FirstEmpty][1] #nextEmpty (3)
            userData = int(input("Enter a value")) #userData (43)
            LinkedList[FirstEmpty][0] = userData #data(43)
            LinkedList[FirstEmpty][1] = FirstNode #point (1)
            FirstNode = FirstEmpty
            FirstEmpty = nextEmpty

def OutputLinkedList():
    global LinkedList
    global FirstNode
    global FirstEmpty
    CurrentPointer = FirstNode
    while CurrentPointer!=-1:
        print(LinkedList[CurrentPointer][0]) #Data(43)
        CurrentPointer = LinkedList[CurrentPointer][1] #CurrentPointer (1)

InsertData()
OutputLinkedList()


def RemoveData(ItemRemove):
    global LinkedList
    global FirstNode
    global FirstEmpty
    if LinkedList[FirstNode][0] ==ItemRemove :
        NewFirst =LinkedList[FirstNode][1] #NewFirst (1)
        LinkedList[FirstNode][1] = FirstEmpty
        FirstEmpty = FirstNode
        FirstNode = NewFirst
    else:
        if FirstNode !=-1:
            CurrentPointer = FirstNode #(1)
            PreviousNode = -1
            #Search for the node to be removed
            while ItemRemove !=LinkedList[CurrentPointer][0] and CurrentPointer !=-1:
                PreviousNode = CurrentPointer
                CurrentPointer = LinkedList[CurrentPointer][1] #Currentpointer (0)
            if ItemRemove == LinkedList[CurrentPointer][0]:
                LinkedList[PreviousNode][1] = LinkedList[CurrentPointer][1]
                LinkedList[CurrentPointer][0] = -1
                LinkedList[CurrentPointer][1] = FirstEmpty
                FirstEmpty = CurrentPointer

RemoveData(42)
print("After remove")
OutputLinkedList()

