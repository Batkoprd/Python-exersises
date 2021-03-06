"""
Задание:
Лабиринт может быть представлен двухмерной матрицей, где нули представляют области, по которым можно ходить,
а единицы - стены. Вы начинаете движение с верхнего левого угла, а выход находится в самой нижней правой ячейке.
Создайте функцию, которая возвращает истину, если вы можете пройти от одного конца лабиринта до другого.
Двигаться можно только вверх, вниз, влево и вправо. По диагонали двигаться нельзя.

Примеры:

can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]) ➞ true

can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
]) ➞ false
# В этом лабиринте одни тупики!

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
]) ➞ false
# Выход так близко, но недостижим!

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
]) ➞ true

Примечания:
1. В лабиринте размером m x n вы входите в [0, 0] и выходите в [m-1, n-1].
2. За эту задачу можно будет получить дополнительные 10 балов (т.е. всего 20), если сделать визуализацию алгоритма поиска
пути при помощи модуля turtle либо его аналогов.
3. Также эту задачу не обязательно сдавать на repl.it - страницы на гитхабе либо просто файла будет достаточно.
"""


def can_exit(maze: list) -> bool:

    rows = len(maze)
    columns = len(maze[0])
    minimal_path = rows + columns - 1  # длина самого короткого пути из (0,0) в (-1,-1)
    maze_indexes_sum = []  # cуммы координат y + x свободных клеточек

    for row in range(rows):
        for column in range(columns):
            if maze[row][column] == 0:
                maze_indexes_sum.append(row + column)

    path = sorted(maze_indexes_sum)
    res = []

    for i in range(0, len(path)):
        if (path[i] - path[i - 1]) <= 1:  # мы можем ходить только вправо\влево и вверх\вниз, соответственно сумма y+x должна изменяться максимум на единицу
            res.append(True)
        else:
            res.append(False)

    condition = path[-1] == minimal_path - 1  # проверяем, что лабиринт имеет выход в (-1,-1)

    return False not in res and condition


print(
can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]),

can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
]),

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
]),

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
]),
can_exit([
        [0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0]]),

can_exit([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]), sep='\n')
