class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj.protectedVar = 34
print(obj._protectedVar)



class Protected:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()


 #Created class with encapsulation

class example:
    def __init__(self):
        self._protectedVar= 14

obj1= Protected()
obj1.protectedVar = 100
print(obj1.protectedVar)


class second_example:
    def __init__(self):
        self.__privateVar = 4000

    def getPrivate(self):
        print(self.__privateVar)
    def setPrivate(self, private):
        self.__privateVar = private
obj2 = Protected()
obj2.getPrivate()
obj2.setPrivate(32)
obj2.getPrivate()
