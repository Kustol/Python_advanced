import csv
import json

__all__ = ['json2csv']


def json2csv(json_file_path: str, csv_file_path: str) -> None:
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    rows = []
    for access_level, users in data.items():
        for user_id, name in users.items():
            rows.append({'access_level': int(access_level), 'id': int(user_id), 'name': name})
    print(rows)

    with open(csv_file_path, 'w', encoding='utf-8') as csv_file:
        csv_dict = csv.DictWriter(csv_file, fieldnames=['access_level', 'id', 'name'], dialect='excel')
        csv_dict.writeheader()
        csv_dict.writerows(rows)


if __name__ == '__main__':
    json2csv('../Task_2.json', '../Task_2.csv')