# 2. Закодируйте любую строку по алгоритму Хаффмана.

# Знаете, что самое интересное?
# Я написал эту вундервафлю, дак она еще и работает!
# Да не просто работает, а как надо работает!
# В ней ваще все есть, чего я не знал - и класс (мой собственный) и рекурсии (2 шт на секундочку) и деквии и ордереддикт
# Я сам себе поражен, если честно
# От разобранной на уроке фразы кодировка немного отличается, ибо по разному ставим элементы с одинаковой частотой

from collections import Counter, OrderedDict, deque

# создаем класс узел. в нем лежат буква, частота, и правая и левая ветви
class Node:

    def __init__(self, char, freq, left = None, right = None):

        self.char = char
        self.freq = freq
        self.left = left
        self.right= right

# Тут создаем дерево из листочков
def create_nodes(leafs):

    # базовый шаг - мы свернули все до корня
    if len(leafs) == 1:
        pass

    # если еще не все свернули
    else:
        # Возьмем первые два элемента, засунев в новый узел, и воткнем в нужное место,
        # а очередь укорачиваем на эти два первых элемента
        l = leafs.popleft()
        r = leafs.popleft()
        sum_freq = l.freq+ r.freq
        new_node = Node('', sum_freq, left=l, right=r)

        for i,node in enumerate(leafs):

            # ищем узел, перед котороым воткнем новый
            if sum_freq <= node.freq:
                leafs.insert(i, new_node)
                break

        # если не нашли такого узла, то значит в конец добавляем
        else:
            leafs.append(new_node)

        # вызываем саму себя на уроченный список узлов
        create_nodes(leafs)


# здесь будем разворачивать полученное дерево
def go_over(leafs, code_table, code = ''):

    root = leafs
    left = root.left
    right = root.right


    # значение None только в листьях, достаточно проверки по левой или правой ветке
    if left == None:
        code_table[root.char] = code

    # если еще не спустились в самый низ
    else:
        go_over(left, code_table, code + '0') # Налево - сказку говорит
        go_over(right, code_table, code + '1') # Направо - коня потеряешь

def main():


    string = input('Введите строку для кодировки Хаффмана '
                   '\nИли введите -1, чтобы испльзовать строку beep boop beer!'
                   '\n>>: ')

    if string == '-1':
        string = 'beep boop beer!'

    print(f'Выбрана строка: {string}')

    # Каунтер чтобы посчитать вхождения символов
    count = Counter(string)

    # Упорядочим все по возрастанию и засунем в упорядоченный словарь
    ord_count = OrderedDict(sorted(count.items(), key=lambda t: t[1]))

    # Теперь по упорядоченному идем и создаем начальный список листьев
    leafs = deque()
    for key,value in ord_count.items():
        leafs.append(Node(key, value))

    # Создаем дерево
    create_nodes(leafs)

    # тут будем хранить коды
    code_table = dict()

    # проходимся по дереву
    go_over(*leafs, code_table)

    print('\nТаблица кодировки Хаффмана')
    for elem in code_table.items():
        print(elem)

if __name__ == '__main__':
    main()