ArrayNodes=[[0 for X in range(3)] for Y in range(20)]
RootPointer = -1
FreeNode = 0

def AddNode(ArrayNodes, RootPointer, FreeNode):
	NodeData = int(input("Enter the Data: "))
	if FreeNode <= 19:
		ArrayNodes[FreeNode][0] = -1
		ArrayNodes[FreeNode][1] = NodeData
		ArrayNodes[FreeNode][2] = -1
		if RootPointer == -1: # Add to start
			RootPointer = 0
		else:
			Placed = False
			CurrentNode = RootPointer
			while Placed == False:
				if NodeData < ArrayNodes[CurrentNode][1]:
					if ArrayNodes[CurrentNode][0] == -1:
						ArrayNodes[CurrentNode][0] = FreeNode
						Placed = True
					else:
						CurrentNode = ArrayNodes[CurrentNode][0]
				else:
					if ArrayNodes[CurrentNode][2] == -1:
						ArrayNodes[CurrentNode][2] = FreeNode
						Placed = True
					else:
						CurrentNode = ArrayNodes[CurrentNode][2]
		FreeNode = FreeNode + 1
	else:
		print("Tree is full")
	return ArrayNodes, RootPointer, FreeNode

def PrintAll(ArrayNodes):
	for X in range(0, 20):
		print(str(ArrayNodes[X][0]), " ", str(ArrayNodes[X][1]), " ", str(ArrayNodes[X][2]))


for X in range(0,10):
	ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes,RootPointer,FreeNode)

PrintAll(ArrayNodes)

'''
Enter the Data10
Enter the Data5
Enter the Data15
Enter the Data8
Enter the Data12
Enter the Data6
Enter the Data20
Enter the Data11
Enter the Data9
Enter the Data4
1   10   2
9   5   3
4   15   6
5   8   8
7   12   -1
-1   6   -1
-1   20   -1
-1   11   -1
-1   9   -1
-1   4   -1
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
'''

def InOrder(ArrayNodes, RootNode):
	if ArrayNodes[RootNode][0] != -1:
		InOrder(ArrayNodes, ArrayNodes[RootNode][0])
	print(str(ArrayNodes[RootNode][1]))
	if ArrayNodes[RootNode][2] != -1:
		InOrder(ArrayNodes, ArrayNodes[RootNode][2])

InOrder(ArrayNodes,RootPointer)

'''
Enter the Data: 10
Enter the Data: 5
Enter the Data: 15
Enter the Data: 8
Enter the Data: 12
Enter the Data: 6
Enter the Data: 20
Enter the Data: 11
Enter the Data: 9
Enter the Data: 4
1   10   2
9   5   3
4   15   6
5   8   8
7   12   -1
-1   6   -1
-1   20   -1
-1   11   -1
-1   9   -1
-1   4   -1
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
0   0   0
4
5
6
8
9
10
11
12
15
20

'''