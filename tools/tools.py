import csv


class Tools:

    def __init__(self):
        pass

    def csv_pull_key(self, csv_path, key_index):
        with open(csv_path, 'r') as data_file:
            reader = csv.reader(data_file, delimiter=',')
            query_keys = [str(col[key_index]) for col in reader]

        return query_keys

    def csv_writer(self, save_path, data):
        with open(save_path, 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(data)
