#Puzyrkom
import random
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)
print('-'*50)
#
#Puzyrkom
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

#Vstavkami
def insertion_sort(array):

    for i in range(len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -=1

        array[j] = spam

insertion_sort(array)
print(array)
#Privet iz branch7 :)
