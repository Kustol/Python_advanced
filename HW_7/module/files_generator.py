from string import ascii_lowercase, digits
from random import choices, randint
from os import path, mkdir, chdir

__all__ = ['make_files', 'make_ext_files', 'make_files_in_dir']


def make_files(extension: str, min_name_len: int = 6, max_name_len: int = 30,
               min_bytes: int = 256, max_bytes: int = 4096, files_qty: int = 42) -> None:
    for _ in range(files_qty):
        file_name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name_len, max_name_len)))
        file_data = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        with open(rf'{file_name}.{extension}', 'wb') as bin_file:
            bin_file.write(file_data)


def make_files_in_dir(target_dir, **kwargs) -> None:
    if not path.exists(target_dir):
        mkdir(target_dir)
    chdir(target_dir)
    make_ext_files(**kwargs)


def make_ext_files(**kwargs):
    for ext, qty in kwargs.items():
        make_files(ext, files_qty=qty)


if __name__ == '__main__':
    make_files_in_dir('../files', doc=3, jpeg=5, gif=5, txt=5, jpg=5)