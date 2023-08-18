'''
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
Добавьте к задачам 1 и 2 строки документации для классов.
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
'''

class Archive:
    '''Одноэлементный класс. Сохраняет только один экземпляр класса. Сохраняет предыдущие аргументы в списках.'''
    _instance = None

    def __init__(self, num: int, text: str):
        '''Принимает целое число num и текстовую строку, добавляет их к экземпляру класса'''
        # print('init')
        self.num = num
        self.text = text

    def __new__(cls, *args, **kwargs):
        '''
        Сохраняет старый экземпляр на прежнем месте вместо создания нового.
        Добавляет предыдущие аргументы в списки истории
        '''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums = []
            cls._instance.texts = []
        else:
            cls._instance.nums.append(cls._instance.num)
            cls._instance.texts.append(cls._instance.text)
        return cls._instance

    def __str__(self):
        '''Способ вывода пользовательской строки'''
        return (f'Numbers: {", ".join(map(str, self.nums))}, {self.num}\n'
                f'Texts: {", ".join(self.texts)}, {self.text}')

    def __repr__(self):
        '''Метод представления строк разработчиком. Показывает инструкцию по созданию экземпляра.'''
        return f'Archive({self.num}, "{self.text}")'


if __name__ == '__main__':
    elem_1 = Archive(11, 'text_1')
    elem_2 = Archive(22, 'text_2')
    print(elem_2)
    print(f'{elem_2 = }')