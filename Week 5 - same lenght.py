"""
Кодинг-марафон. Задача № 5.

    Напишите функцию, которая возвращает True, если в переданном числе за каждой последовательностью
    единиц следует последовательность нулей той же длины.

Примеры:

same_length (110011100010) ➞ True

same_length (101010110) ➞ False

same_length (111100001100) ➞ True

same_length (111) ➞ False

"""

import itertools


def same_length(number: int) -> bool:
    grouped_list = []
    for item, group in itertools.groupby(str(number)):
        grouped_list.append(item * (len(list(group))))
    print(grouped_list)
    condition = all(len(grouped_list[i]) == len(grouped_list[i + 1]) for i in range(0, len(grouped_list) - 1, 2))
    for i in range(0, len(grouped_list) - 1, 2):
        print(grouped_list[i], grouped_list[i+1])
    return condition and len(grouped_list) % 2 == 0



print(
same_length (1010111000543300),


same_length (101010110),

same_length (111100001100),

same_length (1111), sep='\n')
