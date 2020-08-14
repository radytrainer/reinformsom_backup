nOfV = int(input("Enter number of value: "))
counter10 = 0
start  = True
while start:
    for index in range(start , nOfV):
        indexValue = index + 1
        value = int(input("The value " + str(indexValue) + ": "))
        if value > 0:
            if value == 10:
                counter10 = counter10 + 1
        else:
            print("Value must be greater than 0!")
            start = False
    print("The number of 10 is: " + str(counter10))
