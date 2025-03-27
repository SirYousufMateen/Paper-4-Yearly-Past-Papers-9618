global QueueData
global QueueHead
global QueueTail
QueueData = []
for x in range(0, 20):
    QueueData.append("")
QueueHead = -1
QueueTail = -1
def Enqueue(DataToInsert):
    global QueueData
    global QueueHead
    global QueueTail
    if QueueTail == 19:
        return False
    elif QueueHead == -1:
        QueueHead = 0
    QueueTail = QueueTail + 1
    QueueData.append(DataToInsert)
    return True


def Dequeue():
    global QueueData
    global QueueHead
    global QueueTail
    if QueueHead < 0 or QueueHead > 20 or QueueHead > QueueTail:
        return False
    else:
        QueueHead = QueueHead + 1

        return QueueData[QueueHead - 1]


def StoreItems():
    global QueueData
    global QueueHead
    global QueueTail
    Count = 0
    for X in range(0, 10):
        Data = input("Enter data")
        Total = int(Data[0]) + int(Data[1]) * 3 + int(Data[2]) + int(Data[3]) * 3 +int(Data[4]) + int(Data[5]) * 3
        Total = int(Total / 10)
        if ((Total == 10 and Data[6] == "X") or (Total == int(Data[6]))):
            Result = Enqueue(Data[0:6])
            if (Result == True):
                print("Inserted item")
            else:
                print("Queue full")
        else:
            Count = Count + 1
    print("There were", Count, "Invalid items")


QueueData = []
for x in range(0, 20):
    QueueData.append("")
QueueHead = -1
QueueTail = -1
StoreItems()

Value = Dequeue()
if Value == False:
    print("No data items")
else:
    print("Item code", Value)