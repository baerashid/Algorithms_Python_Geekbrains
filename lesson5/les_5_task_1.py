# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple, defaultdict

# "класс" компания со значениями прибыли поквартально
company = namedtuple('company', 'k1 k2 k3 k4', defaults=[0, 0, 0, 0])
# будем тут хранить все компании, где ключ будет название, а значение - созданный выше класс company
data = defaultdict(company)

N = int(input('Введите количесвто компаний: '))

for _ in range(N):
    name = input('Введите название компании: ')
    # pythonic way - запихнем весь фарш в одну строчку! :)
    pribl = [float(i) for i in input('Введите прибыль за каждый квартал через пробел: ').split()]
    # тут вот по ключу делаем добавочку в словарь, где дефолт_фэктори это наш класс
    data[name] = company(*pribl)

sum_ = 0

#очень хотелось запихнуть средние в data, но тьюпл не изменяем... Если есть идеи как допихнуть в существующий
#словарь data еще одно значение для каждого ключа - расскажите, пожалуйста!
srednie = defaultdict(float)
print('Средняя прибыль по каждой компании')
for comp, pr in data.items():
    srend = (pr.k1 + pr.k2 + pr.k3 + pr.k4) / 4
    srednie[comp] = srend
    print(f'{comp}: {srend}')
    sum_ += srend

print('*'*50)
print(f'Средняя по всем компаниям = {sum_ / N}')

print('*'*50)
print('Список предприятий, с прибылью выше средней')
for comp in srednie:
    #print(comp)
    if srednie[comp]> (sum_ / N):
        print(comp)

print('*'*50)
print('Список предприятий, с прибылью ниже средней')
for comp in srednie:
    #print(comp)
    if srednie[comp]< (sum_ / N):
        print(comp)
