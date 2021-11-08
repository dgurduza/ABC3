import string

from wellOfWisdom import *

#----------------------------------------------
class Riddles(WellOfWisdom):
    def __init__(self):
        self.riddle = ""
        self.answer = ""

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.riddle = strArray[i]
        self.answer = strArray[i + 1]
        i += 2
        #print("Riddle: ", self.riddle, " \nAnswer: ", self.answer)
        return i

    def Print(self):
        print("Riddle: ", self.riddle, " \nAnswer: ", self.answer, "\nQuotient = ", self.Quotient())
        pass

    def Write(self, ostream):
        ostream.write("Riddle: {}  \nAnswer: {} \nQuotient = {}".format \
                          (self.riddle, self.answer, self.Quotient()))
        pass

    def Quotient(self):
        num = 0
        for i in self.riddle:
            if i in string.punctuation:
                num += 1
        return num / len(self.riddle)
        pass
