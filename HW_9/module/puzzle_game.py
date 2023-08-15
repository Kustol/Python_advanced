'''
Угадайка
'''

__all__ = ['play']

puzzle_dict = {
    'В поле лестница лежит, дом по лестнице бежит': ['Поезд', 'поезд'],
    'Чудо-ящик. В нём окно. В том окошечке - кино': ['Телевизор', 'телевизор'],
    'Что за братцы из стекла. Для чая, сока и молока': ['стаканы', 'кружки'],
}


def puzzle(puzzle_text: str, answers: list[str], trials: int) -> int:
    print(puzzle_text)
    try_count = 1
    while trials > 0:
        current_try = input(f'Осталось попыток: {trials}. Ваш ответ: ').lower()
        if current_try in answers:
            print('Верно!')
            return try_count
        print('Неверно!')
        try_count += 1
        trials -= 1
    else:
        print('К сожалению, попыток не осталось. Вы не угадали')
        return trials


def play(puzzle_storage: dict[str, list[str]], trial_amount: int = 3) -> None:
    stats = {}
    for puzzle_text, answer_text in puzzle_storage.items():
        puzzle_result = puzzle(puzzle_text, answer_text, trial_amount)
        stats.update({puzzle_text: puzzle_result})
    show_stat(stats)


def show_stat(stat_dict) -> None:
    print('Статистика: ')
    output = '\n'.join((f'Загадка: {puzzle_text}. '
                        f'{f"Угадана с {trial_count} попытки." if trial_count > 0 else "Не угадана."}'
                        for puzzle_text, trial_count in stat_dict.items()))
    print('\n', output, sep='')


if __name__ == '__main__':
    play(puzzle_dict)