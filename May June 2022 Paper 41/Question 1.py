FileData = [[""] * 2 for i in range(11)]  # string

def ReadHighScores():
    Filename = "HighScore.txt"
    File = open(Filename, 'r')
    for x in range(0, 10):
        FileData[x][0] = File.readline()[:3]
        FileData[x][1] = File.readline()
    File.close

def OutputHighScores():
    for x in range(0, 11):
        Output = str(FileData[x][0]) + " " + str(FileData[x][1])
        print(Output)

ReadHighScores()
OutputHighScores()

'''
FYI 10000

ABC 9092

KEL 8500

PAI 8203

BBB 7980

ACE 7246

GKL 7001

JSI 6490

EIF 6003

DIS 2000

'''
Username = "ABCD"
while len(Username) != 3:
    Username = input("Enter your Username: ")

Score = -1
while Score < 1 or Score > 100000:
    Score = int(input("Enter score: "))

def Arrange(Username, Score):
    for x in range(0, 10):
        if Score > int(FileData[x][1]):
            Temp1 = FileData[x][0]
            Temp2 = FileData[x][1]
            FileData[x][0] = Username
            FileData[x][1] = Score
            Count = x + 1
            while (Count < 10):
                Second1 = FileData[Count][0]
                Second2 = FileData[Count][1]
                FileData[Count][0] = Temp1
                FileData[Count][1] = Temp2
                Temp1 = Second1
                Temp2 = Second2
                Count = Count + 1
            break

Arrange(Username, Score)
OutputHighScores()

'''
FYI 10000

ABC 9092

KEL 8500

PAI 8203

BBB 7980

ACE 7246

GKL 7001

JSI 6490

EIF 6003

DIS 2000

Enter your Username: JKL
Enter score: 9999
FYI 10000

JKL 9999
ABC 9092

KEL 8500

PAI 8203

BBB 7980

ACE 7246

GKL 7001

JSI 6490

EIF 6003
'''


# PART_F

def WriteTopTen():
    Filename = "NewHighScore.txt"
    Filename = open(Filename, 'w')
    for x in range(0, 10):
        Filename.write(str(FileData[x][0]) + '\n')
        Filename.write(str(FileData[x][1]) + '\n')
        Filename.close


WriteTopTen()