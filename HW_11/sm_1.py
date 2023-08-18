'''
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
'''

import time


class MyStr(str):
    '''
    Добавляет имя создателя и время создания в строку
    '''

    def __init__(self, text: str, creator: str):
        '''Выводит начальный журнал на консоль'''
        print('Init started')

    def __new__(cls, text: str, creator: str):
        '''Добавление новых атрибутов - имени создателя и времени создания - к новому экземпляру класса'''
        instance = super().__new__(cls, text)
        instance.creator = creator
        instance.time = time.time()
        return instance

    def __str__(self):
        '''Способ вывода пользовательской строки'''
        return f'"{super().__str__()}" (creator: {self.creator}, created at: {self.time})'

    def __repr__(self):
        '''Метод представления строк разработчиком. Показывает инструкцию по созданию экземпляра.'''
        return f'MyStr("{super().__str__()}", "{self.creator}")'


if __name__ == '__main__':
    my_string = MyStr("Hello world", 'User 1')
    print(my_string)
    print(repr(my_string))