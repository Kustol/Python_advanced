from typing import Callable
from functools import wraps
import random


class GuessNumberError(Exception):
    pass

class OutOfRangeException(GuessNumberError):
    def __init__(self, secret_number: int, min_range: int, max_range: int):
        self.secret_number = secret_number
        self.min_range = min_range
        self.max_range = max_range

    def __str__(self):
        return f'Загаданное число {self.secret_number} находится вне допустимого диапазона ({self.min_range}, {self.max_range})'

class InvalidTrialsException(GuessNumberError):
    def __init__(self, trials_qty: int):
        self.trials_qty = trials_qty

    def __str__(self):
        return f'Количество попыток должно быть положительным числом: {self.trials_qty}'

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

def guess_num(secret_num: int, guess_qty: int):
    for i in range(1, guess_qty + 1):
        answer = int(input(f'Попытка {i}. Угадайте число от 1 до 100: '))
        if answer == secret_num:
            print('Вы угадали!')
            return
        elif answer > secret_num:
            print('Меньше')
        else:
            print('Больше')

    raise InvalidTrialsException(guess_qty)

if __name__ == '__main__':
    try:
        guess_num(10, 3)
    except GuessNumberError as gne:
        print(f"Ошибка в игре: {gne}")