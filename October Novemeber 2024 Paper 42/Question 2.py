class Queue:
    def __init__(self):
        self.QueueArray = []
        for x in range(100):
            self.QueueArray.append(-1)
        self.HeadPointer = -1
        self.TailPointer = 0
TheQueue = Queue()
def Enqueue(AQueue,TheData):
    if AQueue.HeadPointer == -1:
        AQueue.HeadPointer = 0
        AQueue.QueueArray[AQueue.TailPointer]= TheData
        AQueue.TailPointer +=1
        return AQueue,1
    elif AQueue.TailPointer >99:
        return AQueue,-1
    else:
        AQueue.QueueArray[AQueue.TailPointer]= TheData
        AQueue.TailPointer = AQueue.TailPointer + 1
        return AQueue,1

def ReturnAllData(TheQueue):
    Temp = ""
    for count in range(TheQueue.HeadPointer,TheQueue.TailPointer):
        Temp =Temp + str(TheQueue.QueueArray[count]) + " "
    return Temp


for count in range(10):
    inputData = int(input("Enter any integer that is 0 or more"))
    while inputData <0:
        inputData = int(input("Enter any integer that is 0 or more"))

    TheQueue,Returnvalue = Enqueue(TheQueue,inputData)
    if Returnvalue == -1:
        print("Queue is full")
    else:
        print("Item inserted")


print("Data has been added")
print(ReturnAllData(TheQueue))

def Dequeue(AQueue):
    if AQueue.HeadPointer== 100 or AQueue.HeadPointer ==-1 or AQueue.HeadPointer ==AQueue.TailPointer:
        return AQueue,-1
    else:
        Temp = AQueue.QueueArray[AQueue.HeadPointer]
        AQueue.HeadPointer = AQueue.HeadPointer + 1
        return AQueue,Temp

Dequeue(TheQueue)
Dequeue(TheQueue)
print(ReturnAllData(TheQueue))
