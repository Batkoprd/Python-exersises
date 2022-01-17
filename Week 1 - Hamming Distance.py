"""
Кодинг-марафон. Задача № 1.

Условия конкурса - в закрепленной сверху записи канала.

Приз: 10 баллов.

Задание: Создайте функцию, которая принимает две строки и вычисляет расстояние Хэмминга между ними.

Расстояние Хэмминга — число позиций, в которых соответствующие символы двух слов одинаковой длины различны.

Например, в строке «ABCB» на четвертой позиции стоит буква «B», а в строке «ABCD» на той же позиции — буква «D». Расстояние Хэмминга между этими строками — 1.

Примечание: Исходим из того, что передаваемые строки всегда будут одинаковой длины.

Примеры:

hamming_distance("abcde", "bcdef") ➞ 5
hamming_distance("abcde", "abcde") ➞ 0
hamming_distance("strong", "strung") ➞ 1
hamming_distance("ABBA", "abba") ➞ 4
"""

from datetime import datetime
import random
import string
from scipy.spatial.distance import hamming

letters = string.printable
a = ''.join(random.choice(letters) for i in range(1000000))
b = ''.join(random.choice(letters) for j in range(1000000))

time_start = datetime.now()


def hamming_distance(str_x: str, str_y: str):
    dis = 0
    for i in range(len(str_x)):
        if str_x[i] != str_y[i]:
            dis += 1
    return dis
    # return sum(i != j for i, j in zip(str_x, str_y))


time_end = datetime.now()

print(hamming_distance(a, b))

print(f'Total time = {(time_end - time_start)}')



