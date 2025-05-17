class Tree:
    #self.__Name = Name
    #self.__HGrowth = HGrowth
    #self.__MaxH = MaxH
    #self.__MaxW = MaxW
    #self.__EverGreen = EverGreen
    def __init__(self,Name, HGrowth, MaxH, MaxW, EverGreen):
        self.__Name = Name
        self.__HGrowth = HGrowth
        self.__MaxH=MaxH
        self.__MaxW = MaxW
        self.__EverGreen = EverGreen

    def GetTreeName(self):
        return self.__Name
    def  GetGrowth(self):
        return self.__HGrowth
    def  GetMaxHeight(self):
        return self.__MaxH
    def GetMaxWidth(self):
        return self.__MaxW
    def GetEvergreen(self):
        return self.__EverGreen

def ReadData():
    TreeObject = []
    try:
        FileName = open("Trees.txt","r")
        TreeData = []
        TreeData = FileName.read().split("\n")
        SplitTrees = []
        for item in TreeData:
            SplitTrees.append(item.split(","))
        FileName.close()
        for Item in SplitTrees:
            TreeObject.append(Tree(Item[0], int(Item[1]), int(Item[2]), int(Item[3]), Item[4]))
    except IOError:
        print("File is not present")
    return TreeObject

def PrintTrees(item):
    message = " It does not lose its leaves"
    if item.GetEvergreen() == "No":
        message = " It loses its leaves each year"
    print(item.GetTreeName(),"has a maximum height",item.GetMaxHeight(),"a maximum width",item.GetMaxWidth(),"and grows",item.GetGrowth(),message)

TreeObjectArray = ReadData()
PrintTrees(TreeObjectArray[2])

def ChooseTree(Trees):
    MaxHeight= int(input("Enter maximum height"))
    MaxWidth = int(input("Enter maximum width"))
    Evergreen = input("Enter lose (if you want to loses its trees), Enter Keep(if you dont want to loses its trees")
    option = []
    if Evergreen.lower()  == "keep":
        keep = "Yes"
    else:
        keep = "No"
    for item in Trees:
        if item.GetMaxHeight() <=MaxHeight and item.GetMaxWidth()<=MaxWidth and keep == item.GetEvergreen():
            option.append(item)
            PrintTrees(item)
        if len(option) == 0:
            print("No suitable trees")
    Valid = False
    while Valid == False:
        Choice = input("Enter the name of the tree you want")
        for Item in option:
            if Item.GetTreeName() == Choice:
                Valid = True
                Selected = Item
                Start = int(input("Enter the height of the tree you would like to start with in cm"))
                Years = (Selected.GetMaxHeight() - Start) / Selected.GetGrowth()
                print("Your tree should be full height in approximately", Years, "years")

ChooseTree(TreeObjectArray)
