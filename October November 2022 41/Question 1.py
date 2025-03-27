DataArray = [0 for I in range (100)]

def ReadFile():
	global DataArray
	try:
		TextFile = "IntegerData.txt"
		File = open(TextFile, 'r')
		for X in range(0, 100):
			DataArray[X] = File.readline()
			DataArray[X].rstrip('\n')
			DataArray[X] = int(DataArray[X])
		File.close()
	except IOError:
		print("Count not find file")


def FindValues():
	global DataArray
	DataToFind = -1
	while(DataToFind < 1 or DataToFind > 100):
		DataToFind = int(input("Enter a number between 1 and 100: "))
		Total = 0
		for X in range(0, 99):
			if DataArray[X] == DataToFind:
				Total = Total + 1
	return Total

ReadFile()
print("The number appears " + str(FindValues()) + " times")

def BubbleSort():
	global DataArray
	N = 100
	for I in range(N-1):
		for J in range(0, N-I-1):
			if DataArray[J] > DataArray[J+1]:
				DataArray[J], DataArray[J+1] = DataArray[J+1], DataArray[J]

BubbleSort()
print(DataArray)