from extender import *

def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0   # Индекс, задающий текущую строку в массиве
    phrNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)   # преобразование в целое
        #print("key = ", key)
        if key == 1: # признак афоризма
            i += 1
            phrase = Aphorisms()
            i = phrase.ReadStrArray(strArray, i) # чтение афоризма с возвратом позиции за ним
        elif key == 2: # признак пословицы
            i += 1
            phrase = Proverbs()
            i = phrase.ReadStrArray(strArray, i) # чтение пословицы с возвратом позиции за ней
        elif key == 3:  # признак загадки
            i += 1
            phrase = Riddles()
            i = phrase.ReadStrArray(strArray, i)  # чтение загадки с возвратом позиции за ней
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return phrNum
        # Количество пробелами фигур увеличивается на 1
        if i == 0:
            return phrNum
        phrNum += 1
        container.store.append(phrase)
    return phrNum
