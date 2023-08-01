__all__ = ['puzzle', 'storage', 'show_stat']

_data = {}
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
        'В поле лестница лежит, дом по лестнице бежит': ['Поезд', 'поезд'],
        'Чудо-ящик. В нём окно. В том окошечке - кино': ['Телевизор', 'телевизор'],
        'Что за братцы из стекла. Для чая, сока и молока': ['стаканы', 'кружки'],
    }

    for puzzle_text, answer_text in puzzle_dict.items():
        puzzle_result = puzzle(puzzle_text, answer_text, trial_amount)
        add_stat(puzzle_text,puzzle_result)


def add_stat(puzzle_text: str, try_count: int):
    _data.update({puzzle_text:try_count})

def show_stat():
    print('Статистика отгадывания:')
    output = '\n'.join((f'Загадка {puzzle_text}.'
                        f'{f"Угадана с {trial_count} попытки." if trial_count > 0 else "Не разгадана"}'
                        for puzzle_text, trial_count in _data.items()))
    print(output)

if __name__ == '__main__':
    storage()
    show_stat()