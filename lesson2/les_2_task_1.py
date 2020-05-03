"""1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений.
Завершение программы должно выполняться привводе символа '0'
в качестве знака операции. Если пользователь вводит
неверный знак (не '0', '+', '-', '', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль,
если он ввел его вкачестве делителя."""

while True:
    case = input("Выберите операцию (+,-,*,/) или 0 для выхода: ")
    if case not in '+-/*0':
        print("Ошибка, пропробуйте снова")
    else:
        if case == '0':
            print('Выход')
            break
        else:
            c1 = float(input('Введите первое число: '))
            c2 = float(input('Введите второе число: '))

            if case == '+':
                print(f'a + b = {c1+c2}')
            elif case == '-':
                print(f'a - b = {c1-c2}')
            elif case == '*':
                print(f'a * b = {c1*c2}')
            elif c2 != 0:
                print(f'a / b = {c1/c2}')
            else:
                print('Ошибка. Деление на ноль. Попробуйте снова')

