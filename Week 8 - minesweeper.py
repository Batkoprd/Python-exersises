"""
Задание:

Эта задача основана на игре сапер.
Создайте функцию, которая принимает сетку из  "#" и "-". Каждая решетка (#) представляет мину,
а каждое тире (-) - место без мин.

Верните список, в котором каждое тире заменено цифрой, обозначающей количество мин, непосредственно примыкающих к нему
(по горизонтали, вертикали и диагоналям).

Примеры:

num_grid ([
  [«-», «-», «-», «-», «-»],
  [«-», «-», «-», «-», «-»],
  [«-», «-», «#», «-», «-»],
  [«-», «-», «-», «-», «-»],
  [«-», «-», «-», «-», «-»]
]) ➞ [
  [«0», «0», «0», «0», «0»],
  [«0», «1», «1», «1», «0»],
  [«0», «1», «#», «1», «0»],
  [«0», «1», «1», «1», «0»],
  [«0», «0», «0», «0», «0»],
]

num_grid ([
  [«-», «-», «-», «-», «#»],
  [«-», «-», «-», «-», «-»],
  [«-», «-», «#», «-», «-»],
  [«-», «-», «-», «-», «-»],
  ["#", "-", "-", "-", "-"]
]) ➞ [
  [«0», «0», «0», «1», «#»],
  [«0», «1», «1», «2», «1»],
  [«0», «1», «#», «1», «0»],
  [«1», «2», «1», «1», «0»],
  [«#», «1», «0», «0», «0»]
]

num_grid ([
  [«-», «-», «-», «#», «#»],
  [«-», «#», «-», «-», «-»],
  [«-», «-», «#», «-», «-»],
  [«-», «#», «#», «-», «-»],
  [«-», «-», «-», «-», «-»]
]) ➞ [
  [«1», «1», «2», «#», «#»],
  [«1», «#», «3», «3», «2»],
  [«2», «4», «#», «2», «0»],
  [«1», «#», «#», «2», «0»],
  [«1», «2», «2», «1», «0»],
]

"""


def mines_coordinates(minesweeper: list, rows: int, columns: int) -> list:
    mine_row = []
    mine_column = []

    for row in range(rows):
        for column in range(columns):
            if minesweeper[row][column] == '#':
                mine_row.append(row)
                mine_column.append(column)
    coordinates = list(zip(mine_row, mine_column))

    return coordinates


def find_mines(minesweeper: list, row: int, column: int, rows: int, columns: int) -> int:
    mines_nearby = 0

    if (row < (rows - 1) and column < (columns - 1)) and minesweeper[row + 1][column + 1] == '#':
        mines_nearby += 1
    if (row > 0 and column > 0) and minesweeper[row - 1][column - 1] == '#':
        mines_nearby += 1
    if (row < (rows - 1) and column > 0) and minesweeper[row + 1][column - 1] == '#':
        mines_nearby += 1
    if (row > 0 and column < (columns - 1)) and minesweeper[row - 1][column + 1] == '#':
        mines_nearby += 1
    if column > 0 and minesweeper[row][column - 1] == '#':
        mines_nearby += 1
    if column < (columns - 1) and minesweeper[row][column + 1] == '#':
        mines_nearby += 1
    if row < (rows - 1) and minesweeper[row + 1][column] == '#':
        mines_nearby += 1
    if row > 0 and minesweeper[row - 1][column] == '#':
        mines_nearby += 1

    return mines_nearby


def num_grid(minesweeper: list):
    rows = len(minesweeper)
    columns = len(minesweeper[0])
    result = []

    for row in range(rows):
        temp_lst = []
        for column in range(columns):
            temp_lst.append(find_mines(minesweeper, row, column, rows, columns))
        result.append(temp_lst)

    for row, column in mines_coordinates(minesweeper, rows, columns):
        result[row][column] = '#'

    for row in result:
        print('  '.join([str(column) for column in row]))

num_grid([
  ['-', '-', '-', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ['-', '-', '#', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ['-', '-', '-', '-', '-']
])
print()
num_grid([
  ['-', '-', '-', '-', '#'],
  ['-', '-', '-', '-', '-'],
  ['-', '-', '#', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ["#", "-", "-", "-", "-"]
])
print()

num_grid([
  ['-', '-', '-', '#', '#'],
  ['-', '#', '-', '-', '-'],
  ['-', '-', '#', '-', '-'],
  ['-', '#', '#', '-', '-'],
  ['-', '-', '-', '-', '-']
])