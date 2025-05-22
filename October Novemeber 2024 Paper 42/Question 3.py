HighScores = [] #String, 7 x 3
HighScores = [['' for x in range(3)] for y in range(7)]

def ReadData():
    Temp = []
    HighScores = []
    try:
        File = open("HighScoreTable.txt")
        Temp = File.read().split("\n")
        File.close()
    except:
        print("No file found")
    NumberRecords = len(Temp) - 1
    Counter = 0

    while Counter < NumberRecords:
        HighScores.append([Temp[Counter], Temp[Counter + 1], Temp[Counter + 2]])
        Counter = Counter + 3

    return HighScores

def OutputHighScores(HighScores):
    for x in range(0, len(HighScores)):
        print(HighScores[x][0], "reached level", HighScores[x][1], "with a score of", HighScores[x][2])


def SortScores(HighScores):
    Counter = 0
    ArrayLength = len(HighScores)

    for x in range(ArrayLength - 1):
        for y in range(0, ArrayLength - x - 1):
            if int(HighScores[y][1]) < int(HighScores[y + 1][1]):
                HighScores[y], HighScores[y + 1] = HighScores[y + 1], HighScores[y]
            elif int(HighScores[y][1]) == int(HighScores[y + 1][1]):
                if int(HighScores[y][2]) < int(HighScores[y + 1][2]):
                    HighScores[y], HighScores[y + 1] = HighScores[y + 1], HighScores[y]
    return HighScores

HighScores = []
HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)

