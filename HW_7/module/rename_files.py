'''
Напишите функцию группового переименования файлов. Она должна:
 ✔ принимать параметр желаемое конечное имя файлов.
 ✔ при переименовании в конце имени добавляется порядковый номер.
 ✔ принимать параметр количество цифр в порядковом номере.
 ✔ принимать параметр расширение исходного файла.
 ✔ переименование должно работать только для этих файлов внутри каталога.
 ✔ принимать параметр расширение конечного файла.
 ✔ принимать диапазон сохраняемого оригинального имени.
Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''

import os

__all__ = ['rename_files']

def rename_files(files_dir: str, num_digits: int, source_ext: str, target_ext: str,
                 source_name_start: int, source_name_end: int, new_file_name: str = '') -> None:
    # Lambda функция для проверки файла по расширению
    should_rename = lambda file: file.split('.')[-1] == source_ext

    # Получаем список файлов в указанном каталоге и фильтруем по расширению source_ext
    filtered_files = filter(should_rename, os.listdir(files_dir))

    for i, file_name in enumerate(filtered_files):
        # Создаем порядковый номер файла с нужным количеством цифр
        file_number = ''.join('0' for _ in range(num_digits - len(str(i + 1)))) + str(i + 1)

        # Извлекаем имя файла без расширения
        old_name = ''.join(file_name.split('.')[:-1])

        # Формируем новое имя файла согласно заданным параметрам
        new_name = f'{old_name[source_name_start:source_name_end]}{new_file_name}{file_number}.{target_ext}'

        # Переименовываем файл, используя полные пути до старого и нового имени
        os.rename(os.path.join(files_dir, file_name), os.path.join(files_dir, new_name))


if __name__ == '__main__':
    rename_files('../files', 3, 'doc', 'txt', 3, 7, 'new_file')