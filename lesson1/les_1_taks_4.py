"""7. Определить, является ли год, который ввел пользователь, високосным или не високосным."""

year = int(input('Введите год: '))
if (year % 4 == 0):
    print(f'Год {year} - високосный')
else:
    print(f'Год {year} - не високосный')

'Примечание: пользователь идеальный и вводит только года нашей эры'