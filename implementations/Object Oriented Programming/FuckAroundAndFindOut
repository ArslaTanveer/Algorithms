#Method 1

class idk:
    def __init__(self):
        self.idc = 0
        self.idgaf = 0

    def setidc(self, a):
        self.__idc = a

    def setidgaf(self, b):
        self.__idgaf = b


    def getidc(self):
        return (self.__idc)

    def getidgaf(self):
        return (self.__idgaf)

ThisThing = idk()
ThisThing.setidc(1200)
print(ThisThing.getidc())
ThisThing.setidgaf(1000)
print(ThisThing.getidgaf())

class Brain:
    def __init__(self):
        idk.__init__(self)
        self.__irdk = 0
        self.__frainbog = 0

    def setirdk(self, a):
        self.__irdk = a

    def setfrainbog(self, b):
        self.__frainbog = b


    def getirdk(self):
        return (self.__irdk)

    def getfrainbog(self):
        return (self.__frainbog)


Thing = Brain()
Thing.setirdk(1200)
print(Thing.getirdk())
Thing.setfrainbog(1000)
print(Thing.getfrainbog())

#Method 2

class Brain:
    def __init__(self):
        idk.__init__(self)
        self.__irdk = 0
        self.__frainbog = 0


    @property
    def irdk(self):
        return (self.__irdk)
    @property
    def frainbog(self):
        return (self.__frainbog)

    @irdk.setter
    def irdk(self, a):
        self.__irdk = a

    @frainbog.setter
    def frainbog(self, b):
        self.__frainbog = b


Thing = Brain()
Thing.irdk = 1200
print(Thing.irdk)
Thing.frainbog = 1000
print(Thing.frainbog)
