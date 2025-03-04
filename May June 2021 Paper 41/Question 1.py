#PART_A

class node:
	def __init__(self, theData, nextNodeNumber):
		self.Data = theData
		self.nextNode = nextNodeNumber

#PART_B

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]

startPointer = 0
emptyList = 5

#PART_C-1

def outputNodes(linkedList, currentPointer):
	while(currentPointer != -1):
		print(str(linkedList[currentPointer].Data))
		currentPointer = linkedList[currentPointer].nextNode



#PART_C-2

outputNodes(linkedList, startPointer)
'''
1
5
2
6
56
7
'''

#PART_D-1

def addNode(linkedList, currentPointer, emptyList):
	dataToAdd = input("Enter the data to add: ")
	if emptyList <0 or emptyList > 9:
		return False
	else:
		newNode = node(int(dataToAdd), -1)
		linkedList[emptyList] = newNode
		previousPointer = 0
		while(currentPointer != -1):
			previousPointer = currentPointer
			currentPointer = linkedList[currentPointer].nextNode
		linkedList[previousPointer].nextNode = emptyList
		emptyList = linkedList[emptyList].nextNode
		return True


#PART_D-2

returnValue = addNode(linkedList, startPointer, emptyList)
if returnValue == True:
	print("Item successfully added")
else:
	print("Item not added, list full")
outputNodes(linkedList, startPointer)



#PART_D-3

'''
1
5
2
6
56
7
Enter the data to add: 5
Item successfully added
1
5
2
6
56
7
5

'''