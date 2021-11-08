import string

from wellOfWisdom import *

#----------------------------------------------
class Proverbs(WellOfWisdom):
    def __init__(self):
        self.country = ""
        self.proverb = ""

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.proverb = strArray[i]
        self.country = strArray[i+1]
        i += 2
        #print("Proverb: ", self.proverb, " \nCountry: ", self.country)
        return i

    def Print(self):
        print("Proverb: ", self.proverb, " \nCountry: ", self.country, "\nQuotient = ", self.Quotient())
        pass

    def Write(self, ostream):
        ostream.write("Proverb: {}  \nCountry: {} \nQuotient = {}".format \
                          (self.proverb, self.country, self.Quotient()))
        pass

    def Quotient(self):
        num = 0
        for i in self.proverb:
            if i in string.punctuation:
                num += 1
        return num / len(self.proverb)
        pass
