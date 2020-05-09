# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def main():
    size = 10
    arr = [random.randint(0, 49) for _ in range(size)]
    arr1 = [random.randint(0, 5) for _ in range(4)]

    print(arr)
    mergeSort(arr)
    print(f'\nрезультат: \n {arr}')

    #Я не понимаю, почему моя реалиазия не работает, а интернетовская работает!
    #Вроде то же самое делаю ведь! Может кому нибудь интересно, запустите то что ниже:
    #Уже и так и эдак его кручу, не хочет работать как надо
    # split_in_2(arr1, 0)
    # print(f'Своя реализация\nрезульат: \n {arr1}')


def merge_2(L, R): #Слияние 2х упорядоченных массивов в 1 упорядоченный
    i = 0
    j = 0
    res = []
    while True:
        buff_L = L[i]
        buff_R = R[j]
        if buff_L < buff_R:
            res.append(buff_L)
            i += 1
        else:
            res.append(buff_R)
            j += 1
        if i > len(L) - 1 or j > len(R) - 1: #если один из масиивов закончился, то выходим и докидываем остатоки
            break

    if i == j:
        pass #Оба массива закончились одновременно, выходим, ничего делать не надо в рез уже сидит результат
    elif j < i: #сначала закончился левый, значит в правом есть еще элементы, докидываем из в результат и то что в буффере
        res = res + [buff_R] + R[j+1:]
    elif i < j:#наоборот
        res = res + [buff_L] + L[i+1:]

    return res

def split_in_2(arr, num_calls): #Разбиваем на 2 массива пока не получим массив из одного элемента
    print(f'\t'*num_calls, f'Мне дали массив: {arr}')
    if len(arr) > 1:
        print(f'\t'*num_calls,f'Его длина оказалась больше 1: len(arr) = {len(arr)}')
        mid= len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        print(f'\t'*num_calls,f'Я его разделила на 2 массива, средний элемент {arr[mid]}')
        print(f'\t'*num_calls,f'левый - {L}')
        print(f'\t'*num_calls,f'правый - {R}')

        print(f'\t'*num_calls,'Зову сама себя на эти 2 массива...')
        split_in_2(L, num_calls + 1)
        split_in_2(R, num_calls + 1)

        print(f'\t'*num_calls,f'буду сливать в один 2 массива: левый - {L} правый - {R}')
        arr = merge_2(L,R)
        print(f'\t'*num_calls,f'слила, получилось {arr}')

    else:
        print(f'\t'*num_calls,f'массив оказался длиной 1, вот он: {arr}')


def mergeSort(arr): #гребаное правильное решение, не понятно чем отличающееся
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':
    main()
