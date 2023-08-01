from sys import argv
from random import randint as rndi

'''
Угадай число
'''

__all__ = ['get_random_num']

START = 0
STOP = 100
AMOUNT = 2


def get_random_num(start: int, end: int, amount=AMOUNT):
    flag = False
    num = rndi(start, end)
    while amount > 0:
        num_user = int(input('Введи число: '))
        if num_user == num:
            print('Угадал!\t')
            flag = True
        elif num_user < num:
            print('Выбери число больше!\t')
            amount -= 1
        elif num_user > num:
            print('Выбери число меньше! \t')
            amount -= 1
    return flag


if __name__ == '__main__':
    name, *param = argv
    print(get_random_num(*(int(elem) for elem in param)))
