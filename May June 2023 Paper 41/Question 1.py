DataArray = []  # 25 elements Integer

try:
    DataFile = open("Data.txt", 'r')
    for Line in DataFile:
        DataArray.append(int(Line))
    DataFile.close()
except IOError:
    print("Could not find file")


def PrintArray(DataArray):
    output = ""
    for X in range(0, len(DataArray)):
        output = output + str((DataArray[X])) + " "
    print(output)


PrintArray(DataArray)


def LinearSearch(DataArray, DataToFind):
    Count = 0
    for X in range(0, len(DataArray)):
        if (DataArray[X] == DataToFind):
            Count += 1
    return Count


DataToFind = int(input("Enter a number to find "))
while DataToFind < 0 or DataToFind > 100:
    DataToFind = int(input("Enter a number to find "))
NumberTimes = LinearSearch(DataArray, DataToFind)

print("The number", DataToFind, "is found", NumberTimes, "times")