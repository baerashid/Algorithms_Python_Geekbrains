# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random

def main():
    N = int(input('Введите количество вершин: '))
    graph = create_graph(N)
    print(f'Был сгенерирован случайный связный ориентированный граф без петель. Список смежности:'
          f'')
    for i in range(N):
        print(graph[i])

    DFS(graph, int(input('С какой вершины начать обход: ')), [False] * N)


def create_graph(N):
    g = []
    # все доступные вершины
    vertex_list = [i for i in range(N)]

    for i in range(N):

        branch_list = []
        # Выбираем случайное количество случайных вершин, минимум одну из списка вершин, за исключением самой себя
        random_vertexes_to_connect = random.sample(vertex_list[:i] + vertex_list[i + 1:], k=random.randint(1,N-1))

        for j in random_vertexes_to_connect:
            branch_list.append(j)

        # Добавляем сгенерированные ветви в граф
        g.append(branch_list)

    return g


def DFS(graph, start, is_visited):

    # выходим, если нет не посещенных вершин
    if not False in is_visited:
        pass

    # если есть хотя бы одна не посещенная вершина
    else:
        is_visited[start] = True

        for vertex in graph[start]:
            if is_visited[vertex] == False:
                print(f'Вершина {vertex} посещена')
                DFS(graph, vertex, is_visited) # Вызываем саму себя на еще не посещенную вершину


if __name__ == '__main__':
    main()
