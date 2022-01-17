"""
Есть список названий животных:

animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion",
"wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat"]

Напишите функцию, которая будет принимать строку txt и возвращать максимальное количество названий животных,
которые возможно собрать из символов строки.

Примеры:

txt = "goatcode"
count_animals(txt) ➞ 2

# первое животное = "dog"
# оставшиеся символы в строке = "atcoe",
# второе животное = "cat".
# count = 2 (верно)

# если взять  сперва  "goat",
# оставшиеся символы в строке = "code",
# т.е. больше нельзя составить имен животных
# count = 1 (неверно)


count_animals("goatcode") ➞ 2
# "dog", "cat"

count_animals("cockdogwdufrbir") ➞ 4
# "cow", "duck", "frog", "bird"

count_animals("dogdogdogdogdog") ➞ 5
"""

import itertools
animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat"]
sorted_animals = [''.join(sorted(animal)) for animal in animals]
animal_len1, animal_len2 = 3, 4 # в животных только животные с ко-вом символов 3 и 4


def count_animals(txt: str):

    sorted_txt = ''.join(sorted(txt))
    animal_txt1 = list(itertools.combinations(sorted_txt, animal_len1))
    animal_txt2 = list(itertools.combinations(sorted_txt, animal_len2))
    combinations_txt = [''.join(sorted(combination)) for combination in (animal_txt1 + animal_txt2)]
    # print(combinations_txt.count('dgo'))
    # print(combinations_txt.count('act'))
    # print(combinations_txt.count('agot'))
    animals_in_txt = []
    animal_qntty = []
    animal_count = dict()
    for animal in sorted_animals:
        if animal in combinations_txt:
            if len(animal) == animal_len1:
                animal_qntty.append(round(combinations_txt.count(animal) ** (1 / 3), 1))
            else:
                animal_qntty.append(round(combinations_txt.count(animal) ** (1 / 4), 1))
            animals_in_txt.append(animal)
            animal_count = dict(zip(animals_in_txt, animal_qntty))
    condition = len(txt) > len(''.join(animals_in_txt)[:len(sorted_txt)])
    animaltxt = ''.join(animals_in_txt)[:len(sorted_txt)]
    counter = 0
    solution = 0
    if condition:
        for animal in animal_count:
            counter += len(animal) * animal_count[animal]
            if counter <= len(sorted_txt):
                solution += animal_count[animal]
        return int(solution)

    else:
        for animal in sorted_animals:
            if animal in animaltxt:
                counter += 1
        return counter


    # print(animal_count)
    # solution = 0
    # counter = 0
    # for animal in animal_count:
    #     counter += len(animal) * animal_count[animal]
    #     if counter <= len(sorted_txt):
    #         solution += animal_count[animal]
    # return int(solution)

print(count_animals('dogdogdogdogdogdog'),
      count_animals(''.join(animals))
      )

# def count_animals():
#
#
#
#     # animal_update_txt1 = list(itertools.combinations(update_txt(txt), animal_len1))
#     # animal_update_txt2 = list(itertools.combinations(update_txt(txt), animal_len2))
#     # combinations_update_txt = [
#     #     ''.join(sorted(combination)) for combination in (animal_update_txt1 + animal_update_txt2)
#     # ]
#     # print(combinations_update_txt)
#
#     counter = 0
#     #
#     for animal in sorted_animals:
#         if animal in helper_func(animaltxt):
#             counter += 1
#
#     # print(txt)
#
#     # print(sorted('dog') in combinations_txt)
#
#     print(counter)



# count_animals('dogcat')
# count_animals('dogdogdogdog')
# count_animals(''.join(animals))
# print(len(animals))
#
# print(list(itertools.permutations('dogdog', 3)))
# print(list(itertools.combinations('dogdog', 3)))
