#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

array = [random.randint(-15,15) for _ in range(10)]
print('Изначальный массив')
print(array)

pos_min = 0
pos_max = 0
min_ = array[pos_min]
max_ = array[pos_max]

for i,elem in enumerate(array):
    if elem>max_:
        pos_max = i
        max_ = array[pos_max]

    if elem<min_:
        pos_min = i
        min_ = array[pos_min]

array[pos_min], array[pos_max] = array[pos_max], array[pos_min]

print('*'*50)
print("Массив с переставленными мин и макс")
print(array)