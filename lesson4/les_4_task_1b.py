#Для оценки взята следующая задача:
#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

#Реализация 2. В одну строчку
import random
import timeit

SIZE = 10000
print(f'SIZE = {SIZE}')
array = [random.randint(-100,100) for _ in range(SIZE)]

array[array.index((min(array)))], array[array.index((max(array)))] = array[array.index((max(array)))], array[array.index((min(array)))]

# SIZE = 100
# 100 loops, best of 5: 9 nsec per loop
# SIZE = 1000
# 100 loops, best of 5: 9 nsec per loop
# SIZE = 10000
# 100 loops, best of 5: 10 nsec per loop

#Результат такой же. Вывод - не надо придумывать велосипед :)


