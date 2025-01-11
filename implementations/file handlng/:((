#Method 1

class CarShenanigans:      #defining the class
    def __init__(self, d):
        self.__engineSize = 0
        self.__weight = 0
        self.__purchasePrice = d

    def setEngineSize(self, a):
        self.__engineSize = a


    def setWeight(self, b):
        self.__weight = b


    def setPurchasePrice(self, c):
        self.__PurchasePrice = c


    def getEngineSize(self):
        return(self.__engineSize)

    def getWeight(self):
        return(self.__weight)

    def getPurchasePrice(self):
        return(self.__purchasePrice)


ThisCar = CarShenanigans(10)
ThisCar.setPurchasePrice(1200)
print(ThisCar.getPurchasePrice())
ThisCar.setWeight(1000)
print(ThisCar.getWeight())
ThisCar.setEngineSize(2302)
print(ThisCar.getEngineSize())


#Record = CarShenanigans()

#an attempt to edit the values in the class
#Record.__engineSize = 100
#Record.__weight = 200
#Record.__purchasePrice = 1000

#checking if the values were changed however since the variables were made private, no changes to the initial values were done
#print(Record._CarShenanigans__engineSize)


#Method 2

class CarShenanigans:      #defining the class
    def __init__(self, d):
        self.__engineSize = 0
        self.__weight = 0
        self.__purchasePrice = d



    @property
    def engineSize(self):
        return(self.__engineSize)

    @property
    def weight(self):
        return(self.__weight)

    @property
    def purchasePrice(self):
        return(self.__purchasePrice)

    @engineSize.setter
    def engineSize(self, a):
        self.__engineSize = a

    @weight.setter
    def weight(self, b):
        self.__weight = b

    @purchasePrice.setter
    def purchasePrice(self, c):
        self.__PurchasePrice = c


ThisCar = CarShenanigans(100)
ThisCar.weight = 710
print(ThisCar.weight)
ThisCar.engineSize = 232
print(ThisCar.engineSize)
ThisCar.purchasePrice = 1000
print(ThisCar.purchasePrice)



# For Meyhod 1 and 2 they are called differently
# In method 1 the values are stored as a function and read as such

# while using @property makes it treated as variable
