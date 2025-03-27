
class Vehicle:
    # self.__ID string
    # self.__MaxSpeed integer
    # self.__CurrentSpeed integer
    # self.__IncreaseAmount integer
    # self.__HorizontalPosition
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP
        self.__MaxSpeed = MaxSpeedP
        self.__IncreaseAmount = IncreaseAmountP
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if (self.__CurrentSpeed > self.__MaxSpeed):
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

    def OutputCurrentPosition(self):
        print("Current position = ", self.__HorizontalPosition)
        print("Current speed = ", self.__CurrentSpeed)


class Helicopter(Vehicle):
    # VerticalPosition Integer
    # VerticalChange Integer
    # MaxHeight Integer
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VertChangeP, MaxHeightP):
        Vehicle.__init__(self, IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0
        self.__VerticalChange = VertChangeP
        self.__MaxHeight = MaxHeightP

    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if (self.__VerticalPosition > self.__MaxHeight):
            self.__VerticalPosition = MaxHeight
        Vehicle.SetCurrentSpeed(self, Vehicle.GetCurrentSpeed(self) + Vehicle.GetIncreaseAmount(self))
        if (Vehicle.GetCurrentSpeed(self) > Vehicle.GetMaxSpeed(self)):
            Vehicle.SetCurrentSpeed(self, Vehicle.GetMaxSpeed(self))
        Vehicle.SetHorizontalPosition(self, Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self))

    def OutputCurrentPosition(self):
        print("Current position = ", Vehicle.GetHorizontalPosition(self))
        print("Current speed = ", Vehicle.GetCurrentSpeed(self))
        print("Current verticalposition = ", self.__VerticalPosition)


# main
Car = Vehicle("Tiger", 100, 20)
Heli1 = Helicopter("Lion", 350, 40, 3, 100)
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputCurrentPosition()
print("")
Heli1.IncreaseSpeed()
Heli1.IncreaseSpeed()
Heli1.OutputCurrentPosition()