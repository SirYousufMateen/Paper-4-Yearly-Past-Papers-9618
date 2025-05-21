LinkedList = [] #global
FirstNode = -1
FirstEmpty = 0
for x in range(0, 19):
    LinkedList.append([-1, x + 1])
LinkedList.append([-1,-1])

def InsertData():
    global LinkedList
    global FirstNode
    global FirstEmpty
    for _ in range(5):
        if FirstEmpty != -1:
            nextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = int(input("Value: "))
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = nextEmpty
def OutputLinkedList():
    global LinkedList
    global FirstNode
    global FirstEmpty
    CurrentPointer = FirstNode
    Flag = True
    while Flag:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = LinkedList[CurrentPointer][1]
        if CurrentPointer == -1:
            Flag = False

InsertData()
OutputLinkedList()

def RemoveData(ItemToRemove):
    global LinkedList
    global FirstNode
    global FirstEmpty

    if LinkedList[FirstNode][0] == ItemToRemove:
        NewFirst = LinkedList[FirstNode][1]
        LinkedList[FirstNode][1] = FirstEmpty
        FirstEmpty = FirstNode
        FirstNode = NewFirst

    else:
        if FirstNode != -1:
            CurrentPointer = FirstNode
            PreviousNode = -1
            while (ItemToRemove != LinkedList[CurrentPointer][0] and CurrentPointer != -1):
                PreviousNode = CurrentPointer
                CurrentPointer = LinkedList[CurrentPointer][1]

            if ItemToRemove == LinkedList[CurrentPointer][0]:
                LinkedList[PreviousNode][1] = LinkedList[CurrentPointer][1]
                LinkedList[CurrentPointer][0] = -1
                LinkedList[CurrentPointer][1] = FirstEmpty
                FirstEmpty = CurrentPointer

LinkedList = []
FirstNode = -1
FirstEmpty = 0
for x in range(0, 19):
    LinkedList.append([-1, x + 1])
InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()