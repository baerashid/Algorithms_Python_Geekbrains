# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

# добавил

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]
for i in g:
    print(i)
print(len(g))

def deyk_improved(graph, start):
    length = len(graph)
    is_visited = [False]* length
    cost = [float('inf')] * length
    parent = [-1] * length
    to_visit = [[None]] * length # список вершин, чтобы прийти в указанную вершину

    cost[start] = 0
    min_cost = 0
    to_visit[start] = [start] # мы уже в стартовой вершине, значит ее и надо посетить

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if (vertex != 0) and (not is_visited[i]):

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    to_visit[i] = [] #нашли более оптимальный путь, забываем как приходили  в эту вершину до этого
                    to_visit[i] = to_visit[i] + to_visit[start] # берем список вершин от того узла, с которым сейчас работаем
                    to_visit[i].append(i) # добавляем саму вершину, до которой собственно находим мин расстояние

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    return cost, to_visit


s = int(input('От какой вершины идти: '))
minim_rast, vershiny = deyk_improved(g, s)
print(f'минимальные расстояния до вершин: \n{minim_rast}')
print(f'\nВершины, которые надо посетить')
for i in range(len(g)):
    if vershiny[i][0] != None:
        print(f'чтобы попасть в вершину {i}, пройдитесь по: {vershiny[i]}')
    else:
        print(f'В вершину {i} нельзя попасть из вершины {s}')

