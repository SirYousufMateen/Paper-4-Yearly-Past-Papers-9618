global StackData
global StackPointer
StackData = [0,0,0,0,0,0,0,0,0,0]
StackPointer = 0

def PrintArray():
	global StackData
	global StackPointer
	print(StackPointer)
	for x in range (0, 10):
		print(StackData[x])

def Push(DataToPush):
	global StackData
	global StackPointer
	if StackPointer == 10:
		return False
	else:
		StackData[StackPointer] = DataToPush
		StackPointer = StackPointer + 1
		return True

for x in range(0, 11):
	TempNumber = int(input("Enter a number: "))
	if Push(TempNumber) == True:
		print("Stored")
	else:
		print("Stack full")

PrintArray()


def Pop():
	global StackData
	global StackPointer
	if StackPointer == 0:
		return -1
	else:
		ReturnData = StackData[StackPointer - 1]
		StackPointer = StackPointer - 1
		return ReturnData

print(Pop())
print(Pop())

PrintArray()