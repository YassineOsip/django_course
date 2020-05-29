class Calc:
    
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def multiply(self):
        print("n1 * n2")
        print(self.n2 * self.n1)
    
    def summation(self):
        print("n1 + n2")
        print(self.n1+self.n2)
    
    def division(self):
            print("n1 / n2")
            print(self.n1/self.n2)

    def substraction(self):
            print("n1 - n2")
            print(self.n1-self.n2)

calc1 = Calc(2,10)
calc1.multiply()
calc1.division()
calc1.summation()
calc1.substraction()
