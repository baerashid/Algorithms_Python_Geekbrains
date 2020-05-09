# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

def main():
    size = 11
    arr = [random.randint(0, 10) for _ in range(size)]
    print(arr)

    med(arr)
    print(*arr)

def med(arr):
    for i in range(len(arr)//2):
        arr.pop(arr.index(max(arr)))
        arr.pop(arr.index(min(arr)))

    return arr

if __name__ == '__main__':
    main()

