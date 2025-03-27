class Character:
	#private Name as string
	#private XCoordinate as integer
	#private YCoordinate as integer
	def __init__(self, Namep, Xcoord, Ycoord):
		self.__Name = Namep
		self.__XCoordiante = Xcoord
		self.__YCoordinate = Ycoord

	def GetName(self):
		return self.__Name
	def GetX(self):
		return self.__XCoordiante
	def GetY(self):
		return self.__YCoordinate

	def ChangePosition(self, XChange, YChange):
		self.__XCoordiante = self.__XCoordiante + XChange
		self.__YCoordinate = self.__YCoordinate + YChange

Characters = []
TextFile = "Characters.txt"
try:
	File = open(TextFile, 'r')
	for X in range(0, 10):
		Name = File.readline().strip()
		XCoord = File.readline().strip()
		YCoord = File.readline().strip()
		TempC = Character(Name, int(XCoord), int(YCoord))
		Characters.append(TempC)
	File.close()
except:
	print("File not found")


Position = -1
CharacterName = ""
while (Position == -1):
	CharacterInput = input("Enter the Character to move: ").rstrip('\n').lower()
	for Count in range(0, 10):
		Temp = str(Characters[Count].GetName().strip()).lower()
		if (Temp == CharacterInput):
			Position = Count

IsValid = False
while(IsValid != True):
	Move = input("Enter A for left, W for up, S for down, or D for right: ")
	if (Move.upper() == "A"):
		Characters[Position].ChangePosition(-1,0)
		IsValid = True
	elif (Move.upper() == "W"):
		Characters[Position].ChangePosition(0,1)
		IsValid = True
	elif (Move.upper() == "S"):
		Characters[Position].ChangePosition(0,-1)
		IsValid = True
	elif(Move.upper() == "D"):
		Characters[Position].ChangePosition(1,0)
		IsValid = True

print(CharacterName, " has changed coordinate to X = ", str(Characters[Position].GetX()), " Y = ", str(Characters[Position].GetY()))

'''
Enter the Character to move: THOMAS
Enter the Character to move: qui
Enter A for left, W for up, S for down, or D for right: X
Enter A for left, W for up, S for down, or D for right: A
  has changed coordinate to X =  83  Y =  9
'''