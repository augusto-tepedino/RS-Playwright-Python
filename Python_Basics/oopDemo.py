class Calculator:
    # Class variable:
    num = 100

    # defautlt constructor
    def __init__(self, a, b):
        # variables for that object, thus the "self"
        self.firstNumber = a
        self.secondNumber = b
        print("calling automatically when object is created")

    def getData(self):
        print("executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


if __name__ == "__main__":
    obj = Calculator(2, 3)
    obj.getData()
    print(obj.Summation())

    obj1 = Calculator(5, -2)
    obj1.getData()
    print(obj1.Summation())
