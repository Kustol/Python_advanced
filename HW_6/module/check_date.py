'''В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.'''

from sys import argv

__all__ = ['calend']


def is_leap_year(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def calend(str_date: str) -> bool:
    day, month, year = map(int, str_date.split('.'))
    if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
        return False

    if month in (4, 6, 9, 11) and day > 30:
        return False

    if month == 2 and is_leap_year(year) and day > 29:
        return False

    if month == 2 and not is_leap_year(year) and day > 28:
        return False

    return True


if __name__ == '__main__':
    file_name, *input_date = argv
    print(f'Дата {"существует" if calend(input_date[0]) else "не существует"}.')
