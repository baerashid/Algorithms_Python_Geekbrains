# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

array = [random.randint(0,10) for _ in range(7)]
print('Изначальный массив')
print(array)

pos_min = 0
pos_max = 0
min_ = array[pos_min]
max_ = array[pos_max]

#ищем позицию мин и макс элемента
for i,elem in enumerate(array):
    if elem>max_:
        pos_max = i
        max_ = array[pos_max]

    if elem<min_:
        pos_min = i
        min_ = array[pos_min]

# Считаем сумму
sum = 0
if pos_min < pos_max:
    for i in range(pos_min + 1, pos_max):
        sum += array[i]
if pos_max < pos_min:
    for i in range(pos_max + 1, pos_min):
        sum += array[i]

print(f'Сумма между макс и мин элем = {sum}')


