# ----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    # def ReadStrArray(self, strArray):

    def Print(self):
        print("Container is store", len(self.store), "phrases:")
        for phrases in self.store:
            phrases.Print()
        print("Container contains  = ", self.DeletingNullElements())
        for phrases in self.store:
            if phrases != None:
             phrases.Print()
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} phrases:\n".format(len(self.store)))
        for phrases in self.store:
            phrases.Write(ostream)
            ostream.write("\n")
        ostream.write("Arithmetic mean = {}\n".format(self.ArithmeticMeanOfQuotients()))
        ostream.write("Container contains  = {} phrase(s)\n".format(self.DeletingNullElements()))
        for phrases in self.store:
            if phrases != None:
                phrases.Write(ostream)
                ostream.write("\n")
        pass

    def ArithmeticMeanOfQuotients(self):
        average = 0.0
        quan = 0
        for phrase in self.store:
            quan += phrase.Quotient()
        return quan / len(self.store)

    def DeletingNullElements(self):
        mean = self.ArithmeticMeanOfQuotients()
        length = len(self.store)
        index = 0
        for i in self.store:
            if i.Quotient() < mean:
                self.store[index] = None
                length = length - 1
            index=index+1;
        return length