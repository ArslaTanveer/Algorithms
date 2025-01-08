import pickle
class CarRecord:
    def __init__(self):
        self.vehicleName = ""
        self.vehicleId = 0


Car = [CarRecord() for i in range (100)]

file = open("CarFile.DAT", 'wb')
for j in range(100):
    pickle.dump(Car[j], file)

file.close()

Car = []
file = open("CarFile.DAT", 'rb')
for i in range(100):
    Car.append(pickle.load(file))
file.close()

ThisCar = CarRecord()

file = open("CarFile.DAT", 'rb+')
location = hash(ThisCar.vehicleId)    #the next free location(memory address) is calculated using a hashing algorithm
file.seek(location)                   #that free location inn the file is pointed to
pickle.dump(ThisCar, file)            #a record is inserted in that free location
file.close()

file = open("CarFile.DAT", 'rb')
file.seek(location)
ThatCar = pickle.load(file)
file.close()
