#PART_A

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

#PART_B-1

def linearSearch(searchValue):
	for x in range(0, 10):
		if arrayData[x] == searchValue:
			return True
	return False

#PART_B-2

searchValue = int(input("Enter the number to search for: "))
returnValue = linearSearch(searchValue)
if returnValue == True:
	print("It was found")
else:
	print("It was not found")


#PART_B-3

'''
Enter the number to search for: 8
It was found

Enter the number to search for: 99
It was not found
'''


#PART_C

def bubbleSort():
	for x in range (0, 10):
		for y in range(0, 9):
			if theArray[y] < theArray[y + 1]:
				temp = theArray[y]
				theArray[y] = theArray[y + 1]
				theArray[y + 1] = temp