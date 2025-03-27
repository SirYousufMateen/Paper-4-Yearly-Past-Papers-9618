
StackVowel = [] #string 100
StackConsonant = [] #string 100

global VowelTop #integer
global ConsonantTop #integer

def PushData(Letter):
	global VowelTop
	global ConsonantTop
	if Letter == "a" or Letter == "e" or Letter == "i" or Letter == "o" or Letter == "u":
		if VowelTop == 100:
			print("Vowel stack full")
		else:
			StackVowel.append(Letter)
			VowelTop = VowelTop + 1
	else:
		if ConsonantTop == 100:
			print("Consonant stack full")
		else:
			StackConsonant.append(Letter)
			ConsonantTop = ConsonantTop + 1

def ReadData():
	try:
		DataFile = open("StackData.txt")
		for Line in DataFile:
			PushData(Line.strip())
		DataFile.close()
	except:
		print("File not found")


def PopVowel():
	global VowelTop
	global ConsonantTop
	if VowelTop - 1 >= 0:
		VowelTop = VowelTop - 1
		DataToReturn = StackVowel[VowelTop]
		del StackVowel[-1]
		return DataToReturn
	else:
		return "No data"


def PopConsonant():
	global VowelTop
	global ConsonantTop
	if ConsonantTop - 1 >= 0:
		ConsonantTop = ConsonantTop - 1
		DataToReturn = StackConsonant[ConsonantTop]
		del StackConsonant[-1]
		return DataToReturn
	else:
		return "No data"



#main
VowelTop = 0
ConsonantTop = 0
ReadData()
Letters = ""
Flag = False

for x in range(0, 5):
	Flag = False
	while Flag == False:
		Choice = input("Vowel or Consonant").lower()
		if Choice == "vowel":
			DataAccessed = PopVowel()
			if DataAccessed != "No data":
				Letters = Letters + DataAccessed
				Flag = True
			else:
				print("No vowels left")
		elif Choice == "consonant":
			DataAccessed = PopConsonant()
			if DataAccessed != "No data":
				Letters = Letters + DataAccessed
				Flag = True
		else:
			print("No consonants left")

print(Letters)