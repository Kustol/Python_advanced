import random

__all__ = ['num_pairs_to_file']

MIN_NUM = -1000
MAX_NUM = 1000


def num_pairs_to_file(file_name='num_pairs.txt', limit=1000) -> None:
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(limit + 1):
            first_int = random.randint(MIN_NUM, MAX_NUM)
            second_float = random.uniform(MIN_NUM, MAX_NUM)
            file.write(f'{first_int}|{second_float}\n')


if __name__ == '__main__':
    num_pairs_to_file('../num_pairs.txt')