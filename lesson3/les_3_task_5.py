# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

# Формируем начальный массив, чтобы и положительные были и отрицательные элементы
array = [random.randint(0,15) for _ in range(5)]
array += ([random.randint(-15,-1) for _ in range(5)])
print(array)

#Признак наличия отрицательного элемента в массиве
flag = False
for i, elem in enumerate(array):
    if elem < 0:
        #Как только нашли первый отрицательный - поднимаем флаг
        if flag == False:
            flag = True
            max_neg = elem
            pos_max_neg = i

        if flag == True and elem > max_neg:
            max_neg = elem
            pos_max_neg = i

if flag == True:
    print(f'Максимальный отрицательный элемент = {max_neg}, его позиция: {pos_max_neg}')
else:
    #в задании не сказано, что массив точно имеет отриц. элементы, поэтому проверим все же
    print('В массиве нет отрицательных элементов')