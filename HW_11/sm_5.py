'''
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
'''
class Rectangle:
    '''
    Представление класса Rectangle.
    '''

    def __init__(self, a: float, b: float = None):
        '''
        Принимает стороны прямоугольника. Затем добавляет к экземпляру класса.
        Если указан только один, то предполагается квадрат.
        '''
        self.a = a
        self.b = b if b is not None else a

    def get_perimeter(self) -> float:
        '''Возвращает периметр (сумму всех сторон) прямоугольника/квадрата.'''
        return 2 * (self.a + self.b)

    def get_area(self) -> float:
        '''Возвращает площадь (произведение двух сторон) прямоугольника/квадрата'''
        return self.a * self.b

    def __add__(self, other):
        '''
        Позволяет добавлять один экземпляр прямоугольника к другому по их периметрам.
        Возвращает новый экземпляр класса с новыми сторонами.
        '''
        sum_perimeter = self.get_perimeter() + other.get_perimeter()
        k = sum_perimeter / self.get_perimeter()
        return Rectangle(self.a * k, self.b * k)

    def __sub__(self, other):
        '''
        Позволяет вычесть один экземпляр прямоугольника из другого по их периметрам.
        Возвращает новый экземпляр класса с новыми сторонами.
        '''
        sub_perimeter = abs(self.get_perimeter() - other.get_perimeter())
        k = sub_perimeter / self.get_perimeter()
        return Rectangle(self.a * k, self.b * k)

    def __eq__(self, other):
        '''Возвращает, равен ли экземпляр прямоугольника другому по его площади или нет'''
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        '''Возвращает площадь экземпляра прямоугольника, меньшую, чем у других'''
        return self.get_area() < other.get_area()

    def __le__(self, other):
        '''Возвращает площадь экземпляра прямоугольника, меньшую или равную площади другого экземпляра'''
        return self.get_area() <= other.get_area()

    def __repr__(self):
        return f'Rectangle({self.a}, {self.b})'

    def __str__(self):
        if self.a == self.b:
            return f'Square with side {self.a}'
        else:
            return f'Rectangle with sides {self.a} and {self.b}'


if __name__ == '__main__':
    rect_1 = Rectangle(10, 15)
    rect_2 = Rectangle(20, 30)
    rect_3 = rect_1 + rect_2
    rect_4 = rect_2 - rect_1

    print(f'{rect_3.a = }, {rect_3.b = }, {rect_3.get_perimeter()}')
    print(f'{rect_4.a = }, {rect_4.b = }, {rect_4.get_perimeter()}')

    print(rect_1 < rect_2)
    print(rect_1 >= rect_2)

    print(rect_1)