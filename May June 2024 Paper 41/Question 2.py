class Tree:
    def __init__(self, Name, HGrowth, MaxH, MaxW, PEvergreen):
        self.__TreeName = Name
        self.__HeightGrowth = HGrowth
        self.__MaxHeight = MaxH
        self.__MaxWidth = MaxW
        self.__Evergreen = PEvergreen

	def GetTreeName(self):
		return self.__TreeName

	def GetMaxHeight(self):
		return self.__MaxHeight

	def GetMaxWidth(self):
		return self.__MaxWidth

	def GetGrowth(self):
		return self.__HeightGrowth

	def GetEvergreen(self):
		return self.__Evergreen


def ReadData():
	TreeObjects = []
	try:
		File = open("Trees.txt")
		TreeData = []
		TreeData = File.read().split("\n")
		SplitTrees = []
		for Item in TreeData:
			SplitTrees.append(Item.split(","))
		File.close()
		for Item in SplitTrees:
			TreeObjects.append(Tree(Item[0], int(Item[1]), int(Item[2]), int(Item[3]), Item[4]))
	except IOError:
		print("invalid file")
	return TreeObjects


def PrintTrees(Item):
	Final = "does not lose its leaves"
	if Item.GetEvergreen() == "No":
		Final = "loses its leaves each year"
		print(Item.GetTreeName(), "has a maximum height", Item.GetMaxHeight(), "a maximumwidth",Item.GetMaxWidth()," and grows", Item.GetGrowth(),"cmayear.It",Final)


TreeObjects = ReadData()
PrintTrees(TreeObjects[0])

def ChooseTree(Trees):
    Evergreen = input("Do you want a tree that loses its leaves (enter lose), or keeps its leaves (enter keep)")
    MaxHeight = int(input("What is the maximum tree height in cm"))
    MaxWidth = int(input("What is the maximum tree width in cm"))
    Options = []
    if Evergreen.lower() == "keep" or Evergreen.lower() == "keep leaves" or Evergreen.lower() == "keeps its leaves":
        keep = "Yes"
    else:
        keep = "No"
    for Item in Trees:
		if Item.GetMaxHeight() <= MaxHeight and Item.GetMaxWidth() <= MaxWidth and keep == Item.GetEvergreen():
			Options.append(Item)
			PrintTrees(Item)
		if len(Options) == 0:
			print("No suitable trees")


Valid = False
while Valid == False:
   Choice = input("Enter the name of the tree you want")
   for Item in Options:
      if Item.GetTreeName() == Choice:
         Valid = True
         Selected = Item
         Start = int(input("Enter the height of the tree you would like to start with in cm"))
         Years =  (Selected.GetMaxHeight() - Start)/Selected.GetGrowth()
         print("Your tree should be full height in approximately", Years,"years")