# Коллекции. Модуль Collection
# Counter - как dict, но значение - частота вхождения ключа
from collections import Counter

# a = Counter()
# b = Counter('abracadabra')
# c = Counter({'red': 2, 'blue': 4})
# d = Counter(cats=4, dogs=5)
#
# print(a, b, c, d, sep='\n')
#
# print(b['z'])
# b['z'] = 0
# print(b)
#
# print(list(b.elements()))
# print(b.most_common(2))
#
# g = Counter(a=4, b=6, c=2, d=0)
# f = Counter(a=3, b=6, c=-2, d=-5)
# g.subtract(f)
# print(g)
# print('*' * 50)
# print(set(g))
# print(dict(g))
# g.clear()
# print(g)
#
# print('*'*50)
# x = Counter(a=3, b=1)
# y = Counter(a=1, b=2)
# print(x+y)
# print(x-y)
# print(x&y)
# print(x|y)
#
# print('*'*50)
# z = Counter(a=3, b=-4)
# print(-z)
# print(+z)

# Deque
# from collections import deque
#
# a = deque()
# b = deque('abcdef')
# c = deque([1,2,3,4,5])
#
# print(a, b, c, sep="\n")
#
# b = deque('abcdef', maxlen=3)
# c = deque([1,2,3,4,5], maxlen=4)
#
# print(b, c, sep="\n")
#
# c.clear()
# print(c)
#
# print('*'*50)
# d = deque([i for i in range(5)], maxlen = 7)
# d.append(5)
# d.appendleft(6)
# print(d)
# d.extend([7,8,9])
# d.extendleft([10,11,12])
# print(d)
#
# print('*'*50)
# f = deque([i for i in range(5)], maxlen = 7)
# x = f.pop()
# y = f.popleft()
# print(f,x,y,sep='\n')
#
# print('*'*50)
# g = deque([i for i in range(5)], maxlen = 7)
# print(g.count(2))
# print(g.index(3))
# g.insert(2, 6)
# print(g)
#
# g.reverse()
# print(g)
#
# g.rotate(3)
# print(g)
#
#
# import random
#
# array = [random.randint(-100,100) for _ in range(10)]
# print(array)
#
# # arr_below = []
# # arr_larger = []
# deq = deque()
#
# for item in array:
#
#     if item >0:
#         deq.append(item)
#     elif item<0:
#         deq.appendleft(item)
# print(deq)
#
# print('*'*50)
# with open('big_log.txt', 'r', encoding='utf-8') as f:
#     last_ten = deque(f, maxlen=10)
# print(last_ten)

# Defaultdict

# from collections import defaultdict
#
# a = defaultdict()
# print(a)
#
# s= 'asdflkjfepoivniunda;kndfsa'
# b = defaultdict(int)
# for i in s:
#     b[i] +=1
# print(b)
#
# list_1 = [('cat',1),('dog',5),('cat',1),('mouse',1),('dog',1)]
# c = defaultdict(list)
# for k,v in list_1:
#     c[k].append(v)
#
# print(c)
#
# list_2 = [('cat',1),('dog',5),('cat',2),('mouse',1),('dog',1),('dog',1),('dog',1),('cat',1)]
# d = defaultdict(set)
# for k,v in list_2:
#     d[k].add(v)
#
# print(d)
#
# f = defaultdict(lambda: 'returnifnokey')
# f.update(rex='dog', tomas='cat')
# print(f)
#
# print(f['rex'])
# print(f['jerry'])

# OrderedDict

# from collections import OrderedDict
#
# a = {'cat': 5, 'dog': 2, 'mouse': 14}
# new_a = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
# print(new_a)
#
# b = {'cat': 5, 'dog': 2, 'mouse': 14}
# new_b = OrderedDict(sorted(b.items(), key=lambda x: x[0], reverse=True))
# print(new_b)
#
# print(new_a == new_b)
#
# new_b.move_to_end('dog', last=False)
# print(new_b)
#
# new_b.popitem(last=False)
# print(new_b)
#
# new_b['cow'] = 3
# print(new_b)
# new_b['cat'] = 7
# print(new_b)
#
# print('*'*50)
#
# new_c = OrderedDict(sorted(a.items(), key = lambda x: len(x[0])))
# print(new_c)
#
# for key in reversed(new_c):
#     print(key, new_c[key], end='\n', sep="-")
#
# from collections import deque, OrderedDict, defaultdict
#
# N = 3000
# with open('big_log.txt', 'r', encoding='utf-8') as f:
#     log = deque(f, maxlen=N)
# print(log)
#
# data = OrderedDict()
# spam = defaultdict(int)
#
# for item in log:
#     ip = item[:-1]
#     if not ip.startswith('192.168'):
#         data[ip] = 1
#         spam[ip] += 1
# print(spam)
# print(data)
#
# data.update(spam)
# print(data)
#
# with open('data.txt', 'w', encoding='utf-8') as f:
#     for key, value in data.items():
#         f.write(f"{key} - {value}\n")

#Namedtuple

# from collections import namedtuple
#
# hero_1 = ('Vasya','Elf', 100, 0.0, 250)
# print(hero_1[4])
#
# class Person:
#     def __init__(self, name, race, health, mana, strength):
#         self.name = name
#         self.race = race
#         self.health = health
#         self.mana = mana
#         self.strength = strength
#
# hero_2 = Person('Sasa', 'Ork', 120, 1.0, 250)
# print(hero_2.mana)
#
# New_Person = namedtuple('New_Person', 'name race health mana strength')
# hero_3 = New_Person('Mike','Human', 130, 12, 44)
#
# print(hero_3.name)
#
# prop = ['name', 'race', '_health', 'mana', 'strength']
# New_Person_1 = namedtuple('New_Person_1', prop, rename=True)
#
# hero_4 = New_Person_1('Mike','Human', 130, 12, 44)
# print(hero_4)
#
# print('*'*50)
# Point = namedtuple('Point', 'x, y, z')
#
# p1 = Point(2, z=3, y=4)
# print(p1)
#
# t = [5, 10, 15]
# p2 = Point._make(t)
# print(p2)
#
# d2 = p2._asdict()
# print(d2)
#
# #p2.x = 6
# p3 = p2._replace(x=6)
# print(p3)
#
# print(p3._fields)
# print('*'*50)
# New_Point = namedtuple('New_point', 'x y z', defaults=[0,0])
# p4 = New_Point(5,7)
# print(p4)
#
# print(p4._field_defaults)
# dct = {'x': 10, 'y': 15, 'z': 20}
# p5 = New_Point(**dct)
# print(p5)
# print(*dct)

#ChainMap
