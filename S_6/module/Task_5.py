'''
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
'''
def puzzle(puzzle_text: str, answers: list[str], trials: int):
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


def storage(trial_amount: int = 3):
    puzzle_dict = {
        'Загадка': ['да', 'конечно'],
        'Ещё загадка': ['нет', 'наверное'],
        'Ну и ещё загадка': ['где', 'что'],
    }

    for puzzle_text, answer_text in puzzle_dict.items():
        puzzle_result = puzzle(puzzle_text, answer_text, trial_amount)
        print(puzzle_result)


if __name__ == '__main__':
    storage()