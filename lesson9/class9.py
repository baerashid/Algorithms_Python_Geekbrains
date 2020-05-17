# from binarytree import tree, bst, Node, build
#
# class MyNode:
#
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
# a = tree(height=4, is_perfect=False)
# print(a)
#
# b = bst(height=3, is_perfect=True)
# print(b)
#
# c = Node(7)
# c.left = Node(3)
# c.right = Node(11)
# c.left.left = Node(1)
# c.left.right = Node(5)
# c.right.left = Node(9)
# c.right.right = Node(13)
# print(c)
#
# d = build([7, 3, 11, 1, 5, 9, 3, None, 2, None, 6])
# print(d)

from binarytree import bst

def search(bin_search_tree, number, path=''):
    if bin_search_tree.value == number:
        return f'Число {number} обнаружено по следующему пути:\nКорень{path}'

    if number < bin_search_tree.value and bin_search_tree.left != None:
        return search(bin_search_tree.left, number, path=f'{path}\nШаг влево <-')

    if number > bin_search_tree.value and bin_search_tree.right != None:
        return search(bin_search_tree.right, number, path=f'{path}\nШаг вправо ->')

    return f'Number {number} is not found in the tree'



bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Введите число для поиска:  '))
print(search(bt, num))
