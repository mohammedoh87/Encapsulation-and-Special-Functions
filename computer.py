class computer:
    def __init__(self):
        self.__max_price = 900
    def sell(self):
        print("The maximum price of the computer is ", self.__max_price)
    def setmaxprice(self, price):
        self.__max_price = price

object1 = computer()
object1.sell()
object1.__max_price = 1000 #ignored
object1.sell()
object1.setmaxprice(1000) #accepted
object1.sell()