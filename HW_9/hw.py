'''
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
'''

import json
from functools import wraps
from random import uniform, randint
from typing import Callable
import csv
import math


def gen_float_trios(file_path: str, min_rows: int = 100, max_rows: int = 1000,
                    min_float: float = -100.0, max_float: float = 100.0) -> None:
    with open(file_path, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(randint(min_rows, max_rows)):
            row = [uniform(min_float, max_float) for _ in range(3)]
            csv_writer.writerow(row)


def add_params_from_csv(func: Callable[[float], float]) -> Callable[[str], list[dict]]:
    @wraps(func)
    def wrapper(csv_file_path: str) -> list[dict]:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            result = []
            for params in csv_reader:
                if not any(params):
                    continue

                a, b, c = map(float, params)
                cur_result = {
                    'params': params,
                    'result': func(a, b, c)
                }
                result.append(cur_result)
            return result

    return wrapper


def log2json(func: Callable) -> Callable[[str], None]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        file_path = f'{func.__name__}.json'
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(result, json_file, indent=2, ensure_ascii=False, default=json_serializable)
        except Exception as e:
            print(f'Произошла ошибка при сохранении в JSON: {e}')

    return wrapper


def json_serializable(obj):
    if isinstance(obj, complex):
        return [obj.real, obj.imag]
    raise TypeError(f'Объект типа "{type(obj)}" не является сериализуемым в формате JSON')


@log2json
@add_params_from_csv
def quadratic_equation(a: float, b: float, c: float) -> float | tuple[float | str, float | str]:
    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return root1, root2
    else:
        d = complex(d, 0)
        root1 = (-b + d ** 0.5) / (2 * a)
        root2 = (-b - d ** 0.5) / (2 * a)
        return root1, root2


if __name__ == '__main__':
    gen_float_trios('number_trios.csv')
    quadratic_equation('number_trios.csv')

