# Puzyrkom
import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)
print('-' * 50)


#
# Puzyrkom
# n = 1
# while n < len(array):
#     for i in range(len(array) - n):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     n += 1
#     print(array)
#
# print(array)

# #Vyborom
# def selection_sort(array):
#
#     for i in range(len(array)):
#         idx_min = i
#
#         for j in range(i + 1, len(array)):
#             if array[j] < array[idx_min]:
#                 idx_min = j
#
#         array[idx_min], array[i] = array[i], array[idx_min]
#         print(array)
#
# selection_sort(array)
# print(array)

# #Vstavkami
# def insertion_sort(array):
#
#     for i in range(len(array)):
#         spam = array[i]
#         j = i
#
#         while array[j - 1] > spam and j > 0:
#             array[j] = array[j - 1]
#             j -=1
#
#         array[j] = spam
#
# insertion_sort(array)
# print(array)
# #Privet iz branch7 :)

# #Shellsort
# def shell_sort(array):
#
#     assert 'Too big array', len(array) < 4000
#
#     def new_increment(array):
#         inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
#
#         while len(array) < inc[-1]:
#             inc.pop()
#
#         while len(inc) > 0:
#             yield inc.pop()
#
#     for increment in new_increment(array):
#         for i in range(increment, len(array)):
#             for j in range(i, increment - 1, -increment):
#                 if array[j - increment] <= array[j]:
#                     break
#                 array[j], array[j - increment] = array[j - increment], array[j]
#
# shell_sort(array)
# print(array)

# Hoars sort
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_arr = []
    m_arr = []
    l_arr = []

    for item in array:

        if item > pivot:
            l_arr.append(item)
        elif item < pivot:
            s_arr.append(item)
        elif item == pivot:
            m_arr.append(item)
        else:
            raise Exception('Smth unforseen happened')

    return quick_sort(s_arr) + m_arr + quick_sort(l_arr)

def quick_sort_no_memory(array, fst, lst):

    if fst >= lst:
        return

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:

        while array[i] <  pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)

#quick_sort_no_memory(array, 0, len(array) - 1)

def reverse_list(array):
    for i in range(len(array)//2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]


reverse_list(array)
array.reverse()
array.sort(reverse=True)
print(array)

t = tuple(random.randint(0, 100) for _ in range(10))
print(t)

t = tuple(sorted(t, reverse=True))
print(t)



