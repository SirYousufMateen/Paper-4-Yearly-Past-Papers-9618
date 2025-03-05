class Picture:
	def __init__(self, DescriptionP, WidthSizeP, HeightSizeP, FrameColourP):
		self.__Description = DescriptionP
		self.__Width = int(WidthSizeP)
		self.__Height = int(HeightSizeP)
		self.__FrameColour = FrameColourP

	def GetDescription(self):
		return self.__Description
	def GetWidth(self):
		return self.__Width
	def GetHeight(self):
		return self.__Height
	def GetColour(self):
		return self.__FrameColour

	def SetDescription(self, DescriptionP):
		self.__Description = DescriptionP

PictureArray = []
for i in range(100):
	PictureArray.append(Picture("",0,0,""))

def ReadData(PictureArray):
	Filename = "Pictures.txt"
	Counter = 0
	try:
		File = open(Filename,"r")
		Description = (File.readline()).strip().lower()
		while(Description != ""):
			Width = int((File.readline()).strip())
			Height = int((File.readline()).strip())
			Frame = ((File.readline()).strip()).lower()
			PictureArray[Counter] = Picture(Description, Width, Height, Frame)
			Description =((File.readline()).strip()).lower()
			Counter = Counter + 1
		File.close()
	except IOError:
		print("Could not find File")
	return Counter, PictureArray

NumberPicturesInArray, PictureArray = ReadData(PictureArray)

FrameColour = input("Input the Frame colour: ").lower()
MaxWidth = int(input("Input the Maximum Width: "))
MaxHeight = int(input("Input the Maximum Height: "))
print("Matches Frames shown")
for Z in range(0, NumberPicturesInArray):
	if PictureArray[Z].GetColour() == FrameColour:
		if(PictureArray[Z].GetWidth() <= MaxWidth):
			if (PictureArray[Z].GetHeight() <= MaxHeight):
				print(PictureArray[Z].GetDescription(), " " , str(PictureArray[Z].GetWidth()), " ", str(PictureArray[Z].GetHeight()))




