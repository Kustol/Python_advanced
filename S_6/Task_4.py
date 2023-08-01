'''
Задача 4
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
'''

def puzzle(puzzle_text:str, answers: list[str], trials: int):
    print(puzzle_text)

    try_count = 1
    while trials > 0:
        current_try = input(f'Осталось попыток: {trials}. Ваш ответ: ')
        if current_try in answers:
            return try_count
        try_count += 1
        trials -= 1
    else:
        return trials


if __name__ == '__main__':
    print(puzzle('Загадка', ['да', 'конечно'], 3))
