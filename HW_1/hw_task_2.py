'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

def input_number():
    i = 2
    count = 0
    NOT_SIMPLE = 1
    MIN = 0
    MAX = 100000
    while True:
        number = int(input('Введите число в диапазоне от 0 до 100000: '))
        if MIN < number < MAX:
            while i <= number - 1:
                if number % i == 0:
                    count += 1
                i += 1
            if count >= NOT_SIMPLE:
                print(f'{number} - составное число')
            else:
                print(f'{number} - число простое')
            break
        else:
            print('Error!')
input_number()