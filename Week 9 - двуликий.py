"""
Задание:

Слово «двуликий» состоит из 8 букв. Байт в двоичном формате имеет 8 бит. Байт может представлять символ.

Мы можем использовать слово «двуликий» для выражения слов в двоичном формате, если используем заглавные буквы как единицы, а строчные — как нули.

Создайте функцию, которая будет переводить слово в виде обычного текста в «двуликий код».

Примеры:

translator("Hi") ➞ "дВулИкий дВУлИкиЙ"
translator("123") ➞ "двУЛикиЙ двУЛикИй двУЛикИЙ"

Примечание: переводите слова, написанные латиницей, и цифры. За перевод кириллицы - дополнительный балл.
"""


def translator(text: str) -> str:
    code = 'двуликий'
    bits = '0'*len(code)
    bin_text = [bits[:-(len(bin(ord(char)))-2)]+bin(ord(char))[2:] for char in text]
    code_text = [[str(char) for char in code] for word in bin_text]

    for i in range(len(bin_text)):
        for j in range(len(bin_text[i])):
            if bin_text[i][j] == '1':
                code_text[i][j] = code_text[i][j].upper()

    return ' '.join([''.join(word) for word in code_text])


print(
    translator("аа"),
    translator("123"), sep='\n'
)

print(bin(ord('а')))