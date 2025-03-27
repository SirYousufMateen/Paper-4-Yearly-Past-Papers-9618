Queue = [-1 for I in range(100)] #Integer
HeadPointer = -1
TailPointer = 0

def Enqueue(Data):
	global Queue
	global TailPointer
	global HeadPointer
	if(TailPointer < 100):
		if HeadPointer == -1:
			HeadPointer = 0
		Queue[TailPointer] = Data
		TailPointer = TailPointer + 1
		return True
	return False

Success = False
for Count in range(1, 21):
	Success = Enqueue(Count)
if(Success == False):
	print("Unsuccessful")
else:
	print("Successful")

def RecursiveOutput(Start):
	if(Start == 0):
		return Queue[Start]
	else:
		return Queue[Start] + RecursiveOutput(Start - 1)


print(str(RecursiveOutput(TailPointer - 1)))


'''
Successful
210

'''