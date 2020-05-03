# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque, defaultdict

#Функция сложения 2х 16тиричных чисел
def add(a1,a2,carry_one):
    K = deque('0123456789ABCDEF')
    #Первое число +
    K.rotate(-tr[a1])

    #Единичка в уме +
    if carry_one==1:
        K.rotate(-carry_one)
        carry_one = 0
        #Если единичка в уме привела к числу больше F
        if K[0]=='0':
            carry_one = 1

    #Второе число +
    for _ in range(tr[a2]):
        K.rotate(-1)
        #Если добавление по одному перевалило через F
        if K[0]=='0':
            carry_one = 1 #Единичка в уме

    return K[0],carry_one

#Look up table
tr = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}


a = list(input('Введите первое число в 16-ричной системе: '))
b = list(input('Введите второе число в 16-ричной системе: '))

#Выровнять длины массивов
if len(a)>len(b):
    for _ in range(len(a)-len(b)):
        b.insert(0,'0')
elif len(a)<len(b):
    for _ in range(len(b)-len(a)):
        a.insert(0,'0')

#Складываем поэлементно
result = []
carry_one = 0
for i in range(-1,-len(a)-1,-1):
    sum_, carry_one = add(a[i],b[i],carry_one)
    result.insert(0,sum_)
if carry_one == 1:
    result.insert(0,'1')

print('Сложение:')
print(result)



