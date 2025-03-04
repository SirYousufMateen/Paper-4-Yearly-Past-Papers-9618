#PART_A

class TreasureChest:
	#Private question : String
	#Private answer : Integer
	#Private points : Integer
	def __init__(self, questionP, answerP, pointsP):
		self.__question = questionP
		self.__answer = answerP
		self.__points = pointsP

	def getQuestion(self):				#PART_C-1
		return self.__question

	def checkAnswer(self, answerP):		#PART_C-2
		if int(self.__answer) == answerP:
			return True
		else:
			return False

	def getPoints(self, attempts):		#PART_C-3
		if attempts == 1:
			return int(self.__points)
		elif attempts == 2:
			return int(self.__points) // 2
		elif attempts == 3 or attempts == 4:
			return int(self.__points) // 4
		else:
			return 0


#PART_B

#arrayTreasure(5) as treasureChest
arrayTreasure = []

def readData():
	filename = "TreasureChestData"
	try:
		file = open(filename,"r")
		dataFetched = (file.readline()).strip()
		while(dataFetched != "" ):
			question = dataFetched
			answer = (file.readline()).strip()
			points = (file.readline()).strip()
			arrayTreasure.append(TreasureChest(question, answer, points))
			dataFetched = (file.readline()).strip()
		file.close()
	except IOError:
		print("Could not find file")



#PART_C-4

readData()

choice = int(input("Pick a treasure chest to open: "))
if choice > 0 and choice < 6:
	result = False
	attempts = 0
	while result == False:
		answer = int(input(f"{arrayTreasure[choice-1].getQuestion()}: "))
		result = arrayTreasure[choice-1].checkAnswer(answer)
		attempts = attempts + 1
	print(int(arrayTreasure[choice-1].getPoints(attempts)))


#PART_C-5

'''
Pick a treasure chest to open: 3
1000*4: 4000
20


Pick a treasure chest to open: 2
100/10: 2
100/10: 2
100/10: 10
3
'''