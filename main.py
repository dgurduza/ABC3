import sys
import string
import time
start_time = time.time()
from extender import *
#----------------------------------------------
if __name__ == '__main__':
    if sys.argv[1] == "-f" and len(sys.argv) == 4:
        inputFileName = sys.argv[2]
        outputFileName = sys.argv[3]
        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()

        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = str.replace("\n", "+=").split("+=")
    elif sys.argv[1] == "-n" and len(sys.argv) == 4:
        size = int(sys.argv[2])
        se = Rnd(size)
        strArray = se.replace("\n", "+=").split("+=")
        strArray.pop()
        outputFileName = sys.argv[3]
    else:
        print("Incorrect command line! You must write: -f <inputFileName> <outputFileName>"
              "or -n <number> <outputFileName>")
        exit()

    print('==> Start')
    container = Container()
    ph = ReadStrArray(container, strArray)
    ofile = open(outputFileName, 'w')
    container.Write(ofile)
    ofile.close()

    print('==> Finish')
    #print("--- %s seconds ---" % (time.time() - start_time))
