'''
Панцифровое число — целое число (в какой-то выбранной системе счисления), в котором каждая цифра данной системы счисления появляется по крайней мере один раз.

Для целей нашей задачи мы будем считать панцифровым целое число в десятичной системе, в котором встречается хотя бы раз каждая цифра от 0 до 9.

Напишите функцию, которая будет принимать целое число и возвращать True, если оно является панцифровым, и False — в противном случае.

Подсказка: подумайте о свойствах панцифрового числа после удаления всех дубликатов.

Примеры:

is_pandigital (98140723568910) ➞ True

is_pandigital (90864523148909) ➞ False: 7 отсутствует.

is_pandigital (112233445566778899) ➞ False
'''


def is_pandigital(number: int) -> str:
    digits = set([digit for digit in '0123456789'])
    number_digits = set([digit for digit in str(number)])
    digit_difference = sorted(digits.difference(number_digits))

    if len(digit_difference) == 1:
        print(
            f'{len(number_digits) == 10}:',
            ''.join(digit_difference), 'отсутствует.'
        )
    elif len(digit_difference) > 1:
        print(
            f'{len(number_digits) == 10}:',
            ', '.join(digit_difference), 'отсутствуют.'
        )
    else:
        print(len(number_digits) == 10)
   


is_pandigital (98140723568910)
is_pandigital(90864523148909)

is_pandigital(1122334455778899)
