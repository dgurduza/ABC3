from random import randint
from extender import *

def Rnd(size):
    indexer = 0
    setr = ""
    while indexer < size:
        key = randint(1, 3)
        if key == 1:  # признак афоризма
            setr += (str(key) + "\n" + RndPhrase() + "\n" + RndWord() + "\n")
            indexer += 1
        elif key == 2:  # признак пословицы
            setr += (str(key) + "\n" + RndPhrase() + "\n" + RndWord() + "\n")
            indexer += 1
        elif key == 3:  # признак загадки
            setr += (str(key) + "\n" + RndPhrase() + "\n" + RndWord() + "\n")
            indexer += 1
    return setr


def RndPhrase():
    setr = ""
    size = randint(1, 50)
    for i in range(0, size):
        setr += str(chr(randint(97, 122)))
    count = randint(1, 4)
    indexer = 0
    while indexer < count:
        index = randint(1, size)
        setr = setr[0:index-1]+str(chr(randint(32, 47)))+setr[index+1:]
        indexer += 1
    return setr


def RndWord():
    setr = ""
    size = randint(1, 8)
    for i in range(0, size):
        setr += str(chr(randint(97, 122)))

    return setr
