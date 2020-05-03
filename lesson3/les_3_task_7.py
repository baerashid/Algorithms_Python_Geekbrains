# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

array = [random.randint(-15,15) for _ in range(10)]
print('Изначальный массив')
print(array)

# Ищем первый минимальный
pos_min1 = 0
min1 = array[pos_min1]
for i,elem in enumerate(array):
    if elem < min1:
        pos_min1 = i
        min1 = elem
print(f'Наименьший элемент: {min1}')

# Выкидываем минимальный по его индексу
array.pop(pos_min1)

# В том, что осталось, ищем второй минимальный
min2 = array[0]
for elem in array:
    if elem < min2:
        min2 = elem
print(f'Второй наименьший элемент: {min2}')

