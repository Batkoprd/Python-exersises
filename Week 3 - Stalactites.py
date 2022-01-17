"""Кодинг-марафон. Задача № 3.

Задание:

Сталактиты свисают с потолка пещеры, а сталагмиты растут из пола.

Создайте функцию, которая определяет, представляет ли ввод «stalactites» (сталактиты) или «stalagmites» (сталагмиты). Если ввод содержит и сталактиты, и сталагмиты, верните «both» («оба»).

Ввод будет двухмерным списком, где 1 представляет кусок камня, а 0 — воздушное пространство.

Примеры:

mineralFormation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]) ➞ "stalactites"

mineralFormation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "stalagmites"

mineralFormation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "both
"""


def mineralFormation(pattern: list) -> str:
    rows = len(pattern)
    formation = ''
    stalactite_row = 0
    stalagmite_row = -1
    for row in range(rows):
        if sum(pattern[stalactite_row]) > 0 and sum(pattern[stalagmite_row]) > 0:
            formation = 'both'
        elif sum(pattern[stalactite_row]) > 0:
            formation = 'stalactites'
        elif sum(pattern[stalagmite_row]) > 0:
            formation = 'stalagmite'

    print(formation)


mineralFormation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
])

mineralFormation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
])

mineralFormation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
])


