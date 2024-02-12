class mystring:
    def __str__(self, String):
        self.String = String
    def getString(self):
        self.String = input()
    def printString(self):
        print(self.String.upper())
mystr = mystring()
mystr.getString()
mystr.printString()