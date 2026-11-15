from oopDemo import Calculator


class ChildImpl(Calculator):
    num2 = 90

    def __init__(self):
        super().__init__(self, 1, 2)

    def Multiplicacion(self):
        return self.firstNumber * self.secondNumber

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj3 = ChildImpl()
print(obj3.getCompleteData())
