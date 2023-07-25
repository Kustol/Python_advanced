import shutil

'''
Задание №8
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
'''
rows = int(input('Введите количество рядов для ёлки: '))
for i in range(rows):
    print(f'{"*" * (2 * i + 1):^{rows * 2}}')
print('')

'''
Задание №9
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
'''
columns = shutil.get_terminal_size().columns
print('ТАБЛИЦА УМНОЖЕНИЯ'.center(columns))
print()
for k in range(2):
    for i in range(2, 10):
        for j in range(k * 4 + 2, k * 4 + 6):
            print(f'{j:<2} x  {i:<2} = {i * j: < 10}\t', end="")
        print('')
    print('')