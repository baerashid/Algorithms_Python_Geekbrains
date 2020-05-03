#Для оценки взята следующая задача:
#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

#Реализация 1
import random
import timeit
import cProfile

def switch(SIZE):
    print(f'SIZE = {SIZE}')
    array = [random.randint(-100, 100) for _ in range(SIZE)]
    pos_min = 0
    pos_max = 0
    min_ = array[pos_min]
    max_ = array[pos_max]

    for i, elem in enumerate(array):
        if elem > max_:
            pos_max = i
            max_ = array[pos_max]

        if elem < min_:
            pos_min = i
            min_ = array[pos_min]

    array[pos_min], array[pos_max] = array[pos_max], array[pos_min]
    return array


SIZE = 10000
array = switch(SIZE)
#cProfile.run('switch(SIZE)')


# SIZE = 100
# 100 loops, best of 5: 9 nsec per loop
# SIZE = 1000
# 100 loops, best of 5: 9 nsec per loop
# SIZE = 10000
# 100 loops, best of 5: 10 nsec per loop
