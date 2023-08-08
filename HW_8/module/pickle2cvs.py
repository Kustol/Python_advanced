import pickle
import csv

__all__ = ['pickle2csv']

def pickle2csv(pickle_file_path: str, csv_file_path: str) -> None:
    with open(pickle_file_path, 'rb') as pickle_file:
        data = pickle.load(pickle_file)


    if isinstance(data, dict):
        headers = set()
        for inner_dict in data.values():
            headers.update(inner_dict.keys())

        with open(csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers, dialect='excel',
                                        quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writeheader()
            csv_writer.writerows(data.values())


if __name__ == '__main__':
    pickle2csv('../Task_2.pickle', '../Task_6.csv')
