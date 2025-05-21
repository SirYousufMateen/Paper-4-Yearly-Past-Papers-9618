class Horse:
    def __init__(self, PName, PMaxFenceHeight, PPercentageSuccess):
        self.__Name = PName #String
        self.__MaxFenceHeight = PMaxFenceHeight #Integer
        self.__PercentageSuccess = PPercentageSuccess #Integer

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

    def Success(self, Height, Risk):
        if Height > self.__MaxFenceHeight:
            return self.__PercentageSuccess * 0.2
        else:
            if Risk == 1:
                return self.__PercentageSuccess
            elif Risk == 2:
                return self.__PercentageSuccess * 0.9
            elif Risk == 3:
                return self.__PercentageSuccess * 0.8
            elif Risk == 4:
                return self.__PercentageSuccess * 0.7
            else:
                return self.__PercentageSuccess * 0.6


Horses = []
Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))
print(Horses[0].GetName())
print(Horses[1].GetName())


class Fence:
    def __init__(self, PHeight, PRisk):
        self.__Height = PHeight  # integer
        self.__Risk = PRisk  # integer

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk

Course = []
for x in range(0, 4):
    Valid = False
    while Valid == False:
        Height = int(input("Enter the height in cm"))
        if(Height >= 70 and Height <= 180):
            Valid = True
    Valid = False
    while Valid == False:
        Risk = int(input("Enter the risk between 1 (easy) and 5 (hard)"))
        if(Risk >= 1 and Risk <= 5):
            Valid = True
    Course.append(Fence(Height, Risk))


for y in range(0, 2):
    for x in range(0, 4):
        Chance = Horses[y].Success(Course[x].GetHeight(), Course[x].GetRisk())
        print(Horses[y].GetName(), "Fence", x + 1, "chance of success is", Chance, "%")

AverageSuccess = []
for y in range(0, 2):
    Total = 0
    for x in range(0, 4):
        Chance = Horses[y].Success(Course[x].GetHeight(), Course[x].GetRisk())
        print(Horses[y].GetName(), "Fence", x + 1, "chance of success is", Chance, "%")
        Total = Total + Chance
    Average = Total / 4
    AverageSuccess.append(Average)
    print(Horses[y].GetName(), "average success rate is", Average, "%")

Highest = AverageSuccess[0]
Winner = -1
for x in range(1, 2):
    if Highest < AverageSuccess[x]:
        Winner = x
        Highest = AverageSuccess[x]
print(Horses[Winner].GetName(), " has the highest average chance of success ")


