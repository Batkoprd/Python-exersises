"""
Кодинг-марафон. Задача № 2.

Задание:

22 октября — ДЕНЬ CAPS LOCK. За исключением этого дня, все предложения должны быть в нижнем регистре. Поэтому напишите функцию для нормализации предложения.

Эта функция должна принимать строку. Если строка состоит только из символов верхнего регистра, переведите их в нижний регистр и добавьте в конце восклицательный знак.

Примечания:
- каждая передаваемая в функцию строка - отдельное предложение
- предложение после нормализации должно начинаться с заглавной буквы
- восклицательный знак добавляем к предложениям, которые переводили из верхнего регистра в нижний.

Примеры:

normalize("CAPS LOCK DAY IS OVER")
➞ "Caps lock day is over!"

normalize("Today is not caps lock day.")
➞ "Today is not caps lock day."

normalize("Let us stay calm, no need to panic.")
➞ "Let us stay calm, no need to panic."

"""

from string import ascii_uppercase as upper
# def normalize(data: str) -> str:
#
#     first_character = data[0]
#
#     for character in data:
#         if character.isupper():
#             data = data.replace(character, character.lower())
#     return first_character.upper() + data[1:] + '!'

test_1 = 'CAPS LOCK DAY IS OVER'
test_2 = 'Today is not caps lock day.'
test_3 = 'Let us stay calm, no need to panic.'
test_4 = 'I love new iPhone 13'
test_5 = 'i Am sIxTeEn eMo GiRL'
def normalize(data: str) -> str:
    words = data.split(' ')
    exeptions = ['iPhone', 'iPad', 'iMac', 'iOs']
    print(words)
    first_character = words[0][0]
    print(first_character)

    for word in words:
        if word not in exeptions:
            for character in word:
                if character.isupper():
                    return first_character.upper() + data[1:].lower() + '!'

    # if data.isupper():
    #     return first_character.upper() + data[1:].lower() + '!'
    # else:
    #     return first_character.upper() + data[1:].lower()


print(normalize(test_4))