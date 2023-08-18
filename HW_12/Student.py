'''
Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
'''

import csv
import json
import os
from os.path import exists
from datetime import datetime


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not value.istitle():
            raise ValueError('Фамилия, Имя, Отчество - должны начинаться с большой буквы')
        elif not value.isalpha():
            raise ValueError('Фамилия, Имя, Отчество - должны содержать только буквы')
        setattr(instance, self.name, value)


class Student:
    MARK_LIMITS = {
        'mark': (2, 5),
        'test': (0, 100)
    }

    first_name = NameValidator()
    last_name = NameValidator()
    patronymic = NameValidator()

    def __init__(self, first_name: str, last_name: str, patronymic: str):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic

        with open('subjects.csv', 'r', encoding='utf-8') as subjects_file:
            self.subjects = list(*csv.reader(subjects_file, dialect='excel'))

        self.data_path = f'students/{self.last_name.lower()}_{self.first_name.lower()}_{self.patronymic.lower()}.json'
        self.journal = self._load_data()

    def log_mark(self, subject: str, mark: int, comment: str = ''):
        self._add_data('mark', subject, mark, comment)

    def log_test(self, subject: str, mark: int, comment: str = ''):
        self._add_data('test', subject, mark, comment)

    def _add_data(self, category: str, subject: str, mark: int, comment: str = ''):
        if subject not in self.subjects:
            print(f'{subject} - invalid subject!')
            return
        if not isinstance(mark, int):
            print(f'{mark} - {category} value should be integer number!')
            return
        if not (self.MARK_LIMITS[category][0] <= mark <= self.MARK_LIMITS[category][1]):
            print(f'{mark} - should be in range {self.MARK_LIMITS[category][0]} - {self.MARK_LIMITS[category][1]}!')
            return
        log_dict = {
            'datetime': datetime.now().strftime("%d-%m-%Y %H:%M"),
            'mark': mark,
            'comment': comment
        }
        self.journal[subject][f'{category}s'].append(log_dict)
        self._dump_data()

    def _load_data(self):
        if exists(self.data_path):
            with open(self.data_path, 'r', encoding='utf-8') as journal_file:
                return json.load(journal_file)
        else:
            return {subject: {'marks': [], 'tests': []} for subject in self.subjects}

    def _dump_data(self):
        os.makedirs('students', exist_ok=True)  # Создание директории, если она не существует
        with open(self.data_path, 'w', encoding='utf-8') as journal_file:
            json.dump(self.journal, journal_file, indent=2, ensure_ascii=False)

    def get_avg_subj_mark(self, subject: str):
        if subject not in self.subjects:
            print(f'{subject} - invalid subject!')
            return None
        return round(self._get_avg_subj('marks', subject), 2)

    def get_avg_mark(self):
        avg_mark = self._get_avg('marks')
        return round(avg_mark, 2) if avg_mark is not None else None

    def get_avg_subj_test(self, subject: str):
        if subject not in self.subjects:
            print(f'{subject} - invalid subject!')
            return None
        return round(self._get_avg_subj('tests', subject), 2)

    def get_avg_test(self):
        avg_test = self._get_avg('tests')
        return round(avg_test, 2) if avg_test is not None else None

    def _get_avg(self, category: str):
        marks = [
            self._get_avg_subj(category, subject) for subject in self.subjects if self._get_avg_subj(category, subject) is not None
        ]
        return sum(marks) / len(marks) if marks else None

    def _get_avg_subj(self, category: str, subject: str):
        logs = self.journal.get(subject, {}).get(category + 's', [])
        if logs:
            return sum(log['mark'] for log in logs) / len(logs)
        return None

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def __str__(self):
        avg_mark = self.get_avg_mark()
        avg_test = self.get_avg_test()
        return (f'Student: {self.get_full_name()}\n'
                f'Average mark: {avg_mark}\n'
                f'Average test mark: {avg_test}')


if __name__ == '__main__':
    student_1 = Student('Виктор', 'Победный', 'Викторович')
    student_1.log_mark('Maths', 5, 'classwork')
    student_1.log_mark('Maths', 3, 'homework')
    student_1.log_mark('Maths', 4, 'classwork')
    student_1.log_test('Literature', 73)
    student_1.log_test('History', 97)
    print(student_1)

    student_2 = Student('Иван', 'Иванов', 'Иванович')  # Проверка невалидных данных
    student_2.log_mark('Invalid', 3, 'work')
    student_2.log_test('Invalid', 105)
    print(student_2)

    student_3 = Student('Анна', 'Смирнова', 'Петровна')
    student_3.log_mark('Chemistry', 3, 'classwork')
    student_3.log_mark('Chemistry', 4, 'homework')
    student_3.log_test('Biology', 78)
    student_3.log_test('Geography', 91)
    print(student_3)
