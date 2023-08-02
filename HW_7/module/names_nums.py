from typing import TextIO

__all__ = ['names_and_nums']


def names_and_nums() -> None:
    with (
        open('../num_pairs.txt', 'r', encoding='utf-8') as num_file,
        open('../nickname.txt', 'r', encoding='utf-8') as names_file,
        open('../names_and_nums.txt', 'a', encoding='utf-8') as res_file
    ):
        len_nums = len(num_file.readlines())
        len_names = len(names_file.readlines())
        for _ in range(max(len_names, len_nums)):
            cur_name = read_or_begin(names_file)
            cur_num_1, cur_num_2 = map(float, read_or_begin(num_file).split('|'))
            mul_nums = cur_num_1 * cur_num_2
            if mul_nums > 0:
                res_file.write(f'{cur_name.upper()} {round(mul_nums)}')
            else:
                res_file.write(f'{cur_name.lower()} | {abs(mul_nums)}\n')


def read_or_begin(file_io: TextIO) -> str:
    text = file_io.readline()
    if not text:
        file_io.seek(0)
        text = file_io.readline()

    return text[:-1]


if __name__ == '__main__':
    names_and_nums()