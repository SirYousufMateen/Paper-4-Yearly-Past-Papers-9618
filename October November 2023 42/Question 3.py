import datetime

class Character:
    # self.__CharacterName string
    # self.__DateOfBirth date
    # self.__Intelligence real
    # self.__Speed integer

    def __init__(self, CName, DBirth, Intell, SpeedP):
        self.__CharacterName = CName
        self.__DateOfBirth = DBirth
        self.__Intelligence = Intell
        self.__Speed = SpeedP

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, NewValue):
        self.__Intelligence = NewValue

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1

    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year


class MagicCharacter(Character):
    # self.__Element String

    def __init__(self, ElementP, CName, DBirth, Intell, SpeedP):
        super().__init__(CName, DBirth, Intell, SpeedP)
        self.__Element = ElementP

    def Learn(self):
        if (self.__Element == "fire" or self.__Element == "water"):
            super().SetIntelligence(super().GetIntelligence() * 1.2)
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence() * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.1)


FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)

FirstCharacter.Learn()
print(FirstCharacter.GetName(), "is", FirstCharacter.ReturnAge(), "years old and has intelligence",
      FirstCharacter.GetIntelligence())

FirstMagic = MagicCharacter("fire", "Light", datetime.datetime(2018, 3, 3), 75, 22)

FirstMagic.Learn()
print(FirstMagic.GetName(), "is", FirstMagic.ReturnAge(), "years old and has intelligence",
      FirstMagic.GetIntelligence())