'''
Угадай число (up)
'''

from typing import Callable
from functools import wraps
import random
from os.path import exists
import json

__all__ = ['guess_num']


def validate(func: Callable) -> Callable[[int, int], None]:
    min_number = 1
    max_number = 100
    min_guess_trials = 1
    max_guess_trials = 10

    @wraps(func)
    def wrapper(secret_num: int, guess_qty: int, *args, **kwargs):
        if not min_number <= secret_num <= max_number:
            secret_num = random.randint(min_number, max_number)
        if not min_guess_trials <= guess_qty <= max_guess_trials:
            guess_qty = random.randint(min_guess_trials, max_guess_trials)

        return func(secret_num, guess_qty, *args, **kwargs)

    return wrapper


def add_param_to_json(func: Callable) -> Callable[[list, dict], int]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_path = f'{func.__name__}_2.json'
        data = []

        if exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

        result = func(*args, **kwargs)
        cur_data = {
            'args': args,
            **kwargs,
            'result': result
        }
        data.append(cur_data)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)

        return result

    return wrapper


def trials(calls_qty: int) -> Callable:
    results = []

    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(calls_qty):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco


@trials(3)
@validate
@add_param_to_json
def guess_num(secret_num: int, guess_qty: int):
    for i in range(1, guess_qty + 1):
        answer = int(input(f'Номер попытки: {i}. Угадайте число от 1 до 100: '))
        if answer == secret_num:
            print('Вы угадали!')
            return
        elif answer > secret_num:
            print('Меньше')
        else:
            print('Больше')

    print('Вы проиграли! Число не угадано.')



if __name__ == '__main__':
    guess_num(10, 3)
