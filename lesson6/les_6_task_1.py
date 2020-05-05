# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import sys
from prettytable import PrettyTable

class varible:
    def __init__(self, name, var): #type, self_memory, el_memory, total_mem
        self.name = name
        self.var = var
        # self.type = type
        # self.value = value
        # self.self_memory = self_memory
        # self.el_memory = el_memory
        # self.total_mem = total_mem

    def calc(self):
        self.type = str(self.var.__class__)
        self.memory = sys.getsizeof(self.var)
        self.el_memory = 0
        if hasattr(self.var, '__iter__'):
            for item in self.var:
                self.el_memory += sys.getsizeof(item)

        self.total_mem = self.memory + self.el_memory


if __name__ == '__main__':
    case = 1#выберите один из вариантов реализации задачи


    if case == 1:# 1 вариант

        import random

        array = [random.randint(-15, 15) for _ in range(10)]
        print('Изначальный массив')
        print(array)

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

        print('*' * 50)
        print("Массив с переставленными мин и макс")
        print(array)

        vars = []
        vars.append(varible('array', array))
        vars.append(varible('pos_min', pos_min))
        vars.append(varible('pos_max', pos_max))
        vars.append(varible('min_', min_))
        vars.append(varible('max_', max_))
        vars.append(varible('i', i))
        vars.append(varible('elem', elem))

        table = PrettyTable(['var_name', 'var_value', 'memory for the var', 'mem for the elements', 'total mem for var','sum for all vars'])

        sum_ = 0
        for item in vars:
            item.calc()
            sum_ += item.total_mem
            table.add_row([item.name, item.var, item.memory, item.el_memory, item.total_mem, sum_])

        print('*'*50)
        print('1st variant')
        print(table)

    if case == 2:# 2 вариант

        import random

        array = [random.randint(-15, 15) for _ in range(10)]
        print('Изначальный массив')
        print(array)

        array[array.index((min(array)))], array[array.index((max(array)))] = array[array.index((max(array)))], array[array.index((min(array)))]

        print('*' * 50)
        print("Массив с переставленными мин и макс")
        print(array)

        vars = []
        vars.append(varible('array', array))

        table = PrettyTable(['var_name', 'var_value', 'memory for the var', 'mem for the elements', 'total mem for var','sum for all vars'])

        sum_ = 0
        for item in vars:
            item.calc()
            sum_ += item.total_mem
            table.add_row([item.name, item.var, item.memory, item.el_memory, item.total_mem, sum_])


        print('\n'*3,'*'*50)
        print('2nd variant')
        print(table)

#РЕЗУЛЬТАТЫ
# **************************************************
# 1st variant
# +----------+---------------------------------------+--------------------+----------------------+-------------------+------------------+
# | var_name |               var_value               | memory for the var | mem for the elements | total mem for var | sum for all vars |
# +----------+---------------------------------------+--------------------+----------------------+-------------------+------------------+
# |  array   | [2, -13, 14, 8, -1, 2, 0, -8, -4, 11] |        184         |         276          |        460        |       460        |
# | pos_min  |                   2                   |         28         |          0           |         28        |       488        |
# | pos_max  |                   1                   |         28         |          0           |         28        |       516        |
# |   min_   |                  -13                  |         28         |          0           |         28        |       544        |
# |   max_   |                   14                  |         28         |          0           |         28        |       572        |
# |    i     |                   9                   |         28         |          0           |         28        |       600        |
# |   elem   |                   11                  |         28         |          0           |         28        |       628        |
# +----------+---------------------------------------+--------------------+----------------------+-------------------+------------------+
#  **************************************************
# 2nd variant
# +----------+------------------------------------+--------------------+----------------------+-------------------+------------------+
# | var_name |             var_value              | memory for the var | mem for the elements | total mem for var | sum for all vars |
# +----------+------------------------------------+--------------------+----------------------+-------------------+------------------+
# |  array   | [-9, 3, 0, 4, 7, 10, -1, 4, 6, 10] |        184         |         276          |        460        |       460        |
# +----------+------------------------------------+--------------------+----------------------+-------------------+------------------+

#Вывод - второй вариант использует меньше памяти, т.к. оперирует только с одним исходным массивом и использует встроенные методы.
