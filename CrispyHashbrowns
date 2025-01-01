def Hash(PrimKey):
    return PrimKey % 10


class AppleOnNewtonsHead:
    def __init__(self):
        self.phoneName = ""
        self.customerId = 0


Customer = AppleOnNewtonsHead()
initial = -1
Table= [initial for a in range(10)]


def Insert(Customer):
    index = Hash(Customer.customerId)
    while Hash(index) != -1:
        index += 1
        if index > 10:
            index = 0
    Table[index] = Customer
    
wanted = input("enter a customer id to search")    
def Search(wanted):
    index = Hash(Customer.customerId)
    flag = bool(False)
    for index in range(0,9):
        if Table[index] == wanted:
            flag = True
            print(f"this customer is found at index {index}")
        elif index > 10:
            index = 0
        else:
            index += 1
    if flag == False:
        print("the customer is not present in the array")
                
