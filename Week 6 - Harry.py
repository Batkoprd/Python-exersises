"""
Задание:

Гарри — почтальон. У него есть почтовый участок размером n * m (матричный / 2D-список). Каждый слот в 2D-списке
представляет количество писем в этом месте. Гарри может идти только вправо и вниз.
Он начинает обход в (0, 0) и заканчивает в (n-1, m-1). n представляет высоту, а m — длину матрицы.
Письма Гарри может брать только там, где находится.

Напишите функцию, возвращающую максимальное количество писем, которое Гарри может подобрать.

Примеры:

harry([[5, 2], [5, 2]]) ➞ 12
# (5+5+2)

harry([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15]
]) ➞ 72
# (1+6+11+12+13+14+15)

harry([[]]) ➞ -1
"""

def filled_path(array: list, maximum, minumum) -> list:

    """
    функция, которая добавляет нули в строки на случай если первая строка пустая\строки разной длины
    [[],               [[0, 0, 0],
     [1],               [1, 0, 0],
     [3, 3, 3],   -->   [3, 3, 3],
     [2, 2]]            [2, 2, 0]]
    """
    maximum = 0
    minumum = 100000
    rows = len(array)
    lengths = [len(array[row]) for row in range(rows)]
    for row in range(rows):
        if len(array[row]) < max(lengths):
            filling = [0] * (max(lengths) - len(array[row]))
            array[row] = array[row] + filling
    for row in array:
        print(' '.join([str(elem) for elem in row]))
    return array


def harry(array: list, maximum, minimum) -> int:

    filled_path(array)

    rows = len(array)
    columns = len(array[0])
    if columns == 0:
        return -1
    else:
        for row in range(1, rows):
            array[row][0] += array[row - 1][0]
        for column in range(1, columns):
            array[0][column] += array[0][column - 1]
        for row in range(1, rows):
            for column in range(1, columns):
                array[row][column] += max(array[row - 1][column],
                                          array[row][column - 1])

        return array[rows - 1][columns - 1]





print(
  harry([[0], 
         [0, 11, 1], 
         [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [6, 7, 8, 9], 
         [0, 0, 0, 0, 15, 0, 0]]),
  sum([11, 2, 7, 8, 9, 15]),
  harry([[100]]),
  harry([[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]), sep = '\n'

)

# примеры из задания:

print(
  harry([[5, 2], 
         [5, 2]]),
  harry([[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15]]),
  harry([[]]), sep = '\n'
)
