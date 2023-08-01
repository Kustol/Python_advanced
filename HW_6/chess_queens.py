'''
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''

from HW_6.module.chess import draw_board, get_successful_arrangements_unique, get_user_queens, are_queens_attacking, \
    get_successful_arrangements


if __name__ == '__main__':
    # # Использование координат вводимых пользователем
    # user_arrangement = get_user_queens()
    #
    # print("Введенная расстановка:")
    # if not are_queens_attacking(user_arrangement):
    #     print("Ферзи не бьют друг друга.")
    # else:
    #     print("Ферзи бьют друг друга.")
    # print("Расстановка:")
    # draw_board(user_arrangement)

    # # Вывод 4 успешных расстановок с отрисовкой доски с рандомной генерацией (катастрофически долго)
    # for i, arrangement in enumerate(get_successful_arrangements(), 1):
    #     print(f"Успешная расстановка {i}:")
    #     draw_board(arrangement)
    #     print()

    # Вывод 4 успешных расстановок с отрисовкой доски с использованием уникальной расстановки (быстрее)
    for i, arrangement in enumerate(get_successful_arrangements_unique(), 1):
        print(f"Успешная расстановка {i}:")
        draw_board(arrangement)
        print()
