from typing import Callable
from functools import wraps
import logging

logging.basicConfig(filename='guess.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

class GuessNumberException(Exception):
    pass

class OutOfRangeException(GuessNumberException):
    def __init__(self, number: int, min_num: int, max_num: int):
        self.number = number
        self.min_num = min_num
        self.max_num = max_num

    def __str__(self):
        return f'Secret number {self.number} is out of range ({self.min_num}, {self.max_num})'

class InvalidTrialsException(GuessNumberException):
    def __init__(self, trials_qty: int):
        self.trials_qty = trials_qty

    def __str__(self):
        return f'Quantity of trials should be a positive number: {self.trials_qty}'

def validate(func: Callable) -> Callable[[int, int], None]:
    min_secret_number = 1
    max_secret_number = 100
    min_guess_trials = 1
    max_guess_trials = 10

    @wraps(func)
    def wrapper(secret_num: int, guess_qty: int, *args, **kwargs):
        if not min_secret_number <= secret_num <= max_secret_number:
            logger.error(f'Secret number {secret_num} is out of range ({min_secret_number}, {max_secret_number})')
            raise OutOfRangeException(secret_num, min_secret_number, max_secret_number)
        if not min_guess_trials <= guess_qty <= max_guess_trials:
            logger.error(f'Quantity of trials should be a positive number: {guess_qty}')
            raise InvalidTrialsException(guess_qty)

        return func(secret_num, guess_qty, *args, **kwargs)

    return wrapper

def log_params(func: Callable) -> Callable[[list, dict], int]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'args: {args}, result: {result}')
        return result

    return wrapper

@validate
@log_params
def guess_num(secret_num: int, guess_qty: int):
    for i in range(1, guess_qty + 1):
        answer = int(input(f'Trial number: {i}. Guess a number between 1 and 100: '))
        if answer == secret_num:
            print('You guessed it!')
            return
        elif answer > secret_num:
            print('Smaller')
        else:
            print('Bigger')

if __name__ == '__main__':
    guess_num(50, 2)
