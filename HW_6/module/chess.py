'''
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''

import random

__all__ = ['are_queens_attacking', 'draw_board', 'get_user_queens', 'gen_rnd_queen_positions',
           'get_successful_arrangements', 'gen_unique_positions', 'get_successful_arrangements_unique']


def are_queens_attacking(queens):
    # Проверка, бьют ли ферзи друг друга по горизонтали, вертикали и диагонали
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or \
                    abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return True
    return False


def draw_board(queens):
    board_size = 8
    crown_symbol = "♛"
    square_symbol = "■"
    print("   " + " ".join([chr(65 + i) for i in range(board_size)]))
    for row in range(1, board_size + 1):
        line = f"{row:2d} "
        for col in range(1, board_size + 1):
            if (row, col) in queens:
                line += f"{crown_symbol} "
            else:
                line += f"{square_symbol} "
        print(line)


def get_user_queens():
    queens = []
    for i in range(8):
        while True:
            try:
                user_input = input(f"Введите координаты ферзя {i + 1} в формате 'строка столбец' (например, '3 5'): ")
                row, col = map(int, user_input.split())
                if 1 <= row <= 8 and 1 <= col <= 8:
                    queens.append((row, col))
                    break
                else:
                    print("Неверные координаты. Введите числа от 1 до 8.")
            except ValueError:
                print("Ошибка ввода. Введите два числа через пробел.")
    return queens


def gen_rnd_queen_positions():
    # Генерация случайной расстановки ферзей
    queens = []
    for _ in range(8):
        queens.append((random.randint(1, 8), random.randint(1, 8)))
    return queens


def get_successful_arrangements():
    successful_arrangements = []
    num_successful = 0

    while num_successful < 4:
        random_queens = gen_rnd_queen_positions()
        if not are_queens_attacking(random_queens):
            successful_arrangements.append(random_queens)
            num_successful += 1

    return successful_arrangements


def gen_unique_positions():
    queens = []
    available_rows = list(range(1, 9))
    for _ in range(8):
        row = random.choice(available_rows)
        available_rows.remove(row)
        col = random.randint(1, 8)
        queens.append((row, col))
    return queens


def get_successful_arrangements_unique():
    successful_arrangements = []
    num_successful = 0

    while num_successful < 4:
        random_queens = gen_unique_positions()
        if not are_queens_attacking(random_queens):
            successful_arrangements.append(random_queens)
            num_successful += 1

    return successful_arrangements
