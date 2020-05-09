# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random


def sort_puzyr(arr):
    for i in range(len(arr)):
        perestanovki = 0
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                perestanovki += 1
        # print(perestanovki)
        if perestanovki == 0:  # Если перестановк не было, то массив упорядочен
            break


size = 10
arr = [random.randint(-100, 99) for _ in range(size)]
print(arr)
sort_puzyr(arr)
print(arr)
