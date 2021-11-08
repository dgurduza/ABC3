import string

from wellOfWisdom import *

#----------------------------------------------
class Aphorisms(WellOfWisdom):
    def __init__(self):
        self.author = ""
        self.aphorism = ""

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.aphorism = strArray[i]
        self.author = strArray[i+1]
        i += 2
        #print("Aphorism: ", self.aphorism, " \nAuthor: ", self.author)
        return i

    def Print(self):
        print("Aphorism: ", self.aphorism, " \nAuthor: ", self.author, "\nQuotient = ", self.Quotient())
        pass

    def Write(self, ostream):
        ostream.write("Aphorism: {}  \nAuthor: {} \nQuotient = {}".format \
                     (self.aphorism, self.author, self.Quotient()))
        pass

    def Quotient(self):
        num = 0
        for i in self.aphorism:
            if i in string.punctuation:
                num += 1
        return num/len(self.aphorism)
        pass
