class myclass:
    __privateVar = 27;
    def __privMeth(self):
        print("I am a Private Method")
    def hello(self):
        print("The value ot the private variable is ", myclass.__privateVar)

object1 = myclass()
object1.hello()
object1.__privateMeth()

