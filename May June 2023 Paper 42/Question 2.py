
CircularQueue = [] #SaleData, 5 items
global NumberOfItems #int
global Head #int
global Tail #int

class SaleData:
	def __init__(self, SaleIDp, Quantityp):
		self.SaleID = SaleIDp #string
		self.Quantity = Quantityp #integer

def Enqueue(RecordToAdd):
	global NumberOfItems #int
	global Head #int
	global Tail #int
	if(NumberOfItems == 5):
		return -1
	else:
		CircularQueue[Tail] = RecordToAdd
		if(Tail == 4):
			Tail = 0
		else:
			Tail +=1
		NumberOfItems +=1
		return 1

def Dequeue():
	global NumberOfItems #int
	global Head #int
	global Tail #int
	RecordRemoved = SaleData("", -1)
	if not(NumberOfItems == 0):
		RecordRemoved = CircularQueue[Head]
		NumberOfItems -=1
		if Head == 4:
			Head = 0
		else:
			Head +=1
	return RecordRemoved


def EnterRecord():
	ID = input("Enter ID")
	QuantityP = input("Enter quantity")
	Record = SaleData(ID, QuantityP)
	if Enqueue(Record) == -1:
		print("Full")
	else:
		print("Stored")

NumberOfItems = 0
Head = 0
Tail = 0
for x in range(0, 5):
	CircularQueue.append((SaleData("",-1)))


EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
ReturnValue = Dequeue()
if ReturnValue.SaleID == "":
	print("No items")
else:
	print(ReturnValue.SaleID, " ", ReturnValue.Quantity)
EnterRecord()

for x in range(0, 5):
	print(CircularQueue[x].SaleID, " ", CircularQueue[x].Quantity)