def ReadData():
    Colours = []
    try:
        File = open("Data.txt")
        Colours = File.read().split("\n")
        File.close()
        return Colours
    except:
        print("No file found")

def FormatArray(DataArray):
    OutputText = ""
    for x in range(0, 45):
        OutputText = OutputText + DataArray[x] + " "
    return OutputText

Colours = ReadData() #string array
print(FormatArray(Colours))
def CompareStrings(First, Second):
    Count = 0
    while True:
        if First[Count] < Second[Count]:
            return 1
        elif First[Count] > Second[Count]:
            return 2
        else:
            Count = Count + 1
def Bubble(DataArray):
    ArrayLength = len(DataArray)

    for x in range(ArrayLength - 1):
        for y in range(0, ArrayLength - x - 1):
            Result = CompareStrings(DataArray[y], DataArray[y + 1])
            if Result == 2:
                DataArray[y], DataArray[y + 1] = DataArray[y + 1], DataArray[y]
    return DataArray

BubbleSorted = Bubble(Colours)
print(FormatArray(BubbleSorted))















