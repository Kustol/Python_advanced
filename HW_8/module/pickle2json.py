import json
import pickle
import os

__all__ = ['pickle2json']


def pickle2json(dir_path: str) -> None:
    json_files = filter(lambda file_name: file_name[-5:] == '.json', os.listdir(dir_path))
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as json_reader:
            data = json.load(json_reader)
        with open(f'{json_file[:-5]}.pickle', 'wb') as pickle_file:
            pickle.dump(data, pickle_file)


if __name__ == '__main__':
    pickle2json('.')