'''
Напишите программу, которая получает целое число и
возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

def main():
    number = int(input('Введите число в десятичной системе исчисления: '))

    def self_hex(number: int) -> str:
        if not number:
            return 'Вводимым должно быть число!'
        result = ''
        hex_letters = list('0123456789abcdef')
        while number > 0:
            result = hex_letters[number % 16] + result
            number //= 16
        return '0x' + result

    print(f'Число {number} в 16-тиричном исчислении равно: {self_hex(number)}')
    print(f'Проверка встроенной функцией hex: {hex(number)}')

# Старт
if __name__ == "__main__":
    main()
