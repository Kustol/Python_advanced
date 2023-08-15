'''
Угадай число
'''

from random import randint

__all__ = ['get_random_num']

MIN_NUM = 0
MAX_NUM = 100
TRIALS = 3


def get_random_num(min_num: int = MIN_NUM, max_num: int = MAX_NUM, tries: int = TRIALS):
    secret_num = randint(min_num, max_num)
    while tries > 0:
        user_number = int(input(f'Осталось попыток: {tries}. Угадайте число от {min_num} до {max_num}: '))
        if user_number == secret_num:
            print('Вы угадали!')
            return True
        elif user_number > secret_num:
            print('Меньше.')
        else:
            print('Больше.')
        tries -= 1
    else:
        print('Не угадали. Попыток не осталось.')
        return False


if __name__ == '__main__':
    get_random_num()