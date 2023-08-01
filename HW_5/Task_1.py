'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
import os

def parse_file_path(file_path):
    path, full_file_name = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(full_file_name)
    return path, file_name, file_extension

if __name__ == '__main__':
    absolute_path = 'C:/Пользователи/smert/PycharmProjects/HW_1/hw_task_1.py'
    path, file_name, file_extension = parse_file_path(absolute_path)
    print('Путь:', path)
    print('Имя файла:', file_name)
    print('Расширение файла:', file_extension)

