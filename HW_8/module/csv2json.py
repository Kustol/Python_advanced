import csv
import json

__all__ = ['csv2json']


def csv2json(csv_file_path: str, json_file_path: str) -> None:
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, dialect='excel')
        data = []
        for i, row in enumerate(csv_reader):
            if i:
                access_level, user_id, name = row
                user_data = {'access_level': int(access_level),
                             'user_id': f'{int(user_id):010}',
                             'name': name.capitalize(),
                             'hash': hash((user_id, name))}

                data.append(user_data)

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    csv2json('../Task_2.csv', '../Task_2.json')