#Part a
global DataStored
global NumberItems

NumberItems = 0
DataStored = []

def Initialise():
    global DataStored
    global NumberItems
    NumberItems = int(input("How many numbers will you enter?"))
    while NumberItems <1 or NumberItems>20:
        NumberItems = int(input("How many numbers will you enter?"))
    for count in range(NumberItems):
        DataStored.append(int(input("Enter number")))


Initialise()
print(DataStored)

def Bubble():
    global DataStored
    global NumberItems
    for count in range(NumberItems):
        for index in range(NumberItems-1):
            if DataStored[index]>DataStored[index+1]:
                temp = DataStored[index]
                DataStored[index] = DataStored[index+1]
                DataStored[index+1] = temp


Bubble()
print(DataStored)
def BinarySearch(DataToFind):
    global DataStored
    global NumberItems
    found = False
    low = 0
    high = NumberItems
    mid = (low + high) // 2
    while low < high:
        if DataToFind == DataStored[mid]:
            return mid
        elif DataToFind > DataStored[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    return -1

searchvalue = int(input("Enter a number to find"))
print(BinarySearch(searchvalue))


